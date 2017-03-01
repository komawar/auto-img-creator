# Copyright Nikhil Komawar
# All Rights Reserved
# Licensed under the MIT license

import os
import random
import string
import sys
import math

def create(num_imgs=None):
    license_type = ["win", "RH", "deb", "suse", "bsd", "other"]
    # build_flag = index of license type
    architecture = ["vec", "ep", "simd", "sisd", "mimd", "misd", "mpmd", "spmd"]
    # desc = auto generate text
    # kernel_id = 23 * index
    # ram_id = 71 * index
    snapshot = ["true", "false"]
    for i in range (1, num_imgs):
        idx_lic = random.randint(0, 5)
        idx_arch = random.randint(0, 7)
        # idx_snapshot =  
        desc = "".join( [random.choice(string.letters) for i in xrange(1500)] )
        label = "image_lable_" + str(i)
        command = "glance image-create --name %s --property license_type=%s --property build_flag=%s --property architecture=%s --property desc=%s --property kernel_id=%s --property ram_id=%s --property snapshot=%s" % (label, license_type[idx_lic], idx_lic, architecture[idx_arch], desc, 23*idx_arch, 71*idx_lic, snapshot[i % 2])
        print command
        os.system(command)

if __name__ == '__main__':
    num_imgs = None
    if sys.argv[1]:
        num_imgs = int(sys.argv[1])
    create(num_imgs=num_imgs)
