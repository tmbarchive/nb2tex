#!/usr/bin/env python

import sys,time,urllib,traceback,glob,os,os.path
from distutils.core import setup, Extension, Command
from distutils.command.install_data import install_data

setup(
        name = 'nb2tex',
        version = '0.1',
        author = "Thomas Breuel",
        description = "iPython Notebook to TeX converter",
        scripts = "nb2tex".split()
     )
