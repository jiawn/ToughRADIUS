#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
sys.path.insert(0,os.path.split(__file__)[0])
from console import models
import argparse,json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--conf', type=str,default='./config.json',dest='conf',help='conf file')
    parser.add_argument('-u','--update',nargs='?', type=bool,default='./config.json',dest='update',help='update option')
    args =  parser.parse_args(sys.argv[1:])    
    if args.update:
        models.update(config=json.loads(open(args.conf,'rb').read())['mysql'])
    else:
        models.install(config=json.loads(open(args.conf,'rb').read())['mysql'])