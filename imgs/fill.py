import os, sys
import numpy as np
from PIL import Image

if __name__=='__main__':
    file = sys.argv[1]
    img = np.array(Image.open(file))
    H, W = img.shape[:2]
    nH, nW = int(W*170/250), W

    out = np.ones((nH, nW, 3), dtype='uint8')*255
    out[(nH-H)//2:(nH-H)//2+H, :W, :] = img[:, :, :3]
    Image.fromarray(out).save(file)
