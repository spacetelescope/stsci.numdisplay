#!/usr/bin/env python
import relic.release
from glob import glob
from numpy import get_include as np_include
from setuptools import setup, find_packages, Extension


version = relic.release.get_info()
relic.release.write_template(version, 'lib/stsci/numdisplay')

setup(
    name = 'stsci.numdisplay',
    version = version.pep386,
    author = 'Warren Hack',
    author_email = 'help@stsci.edu',
    description = 'Package for displaying numpy arrays in DS9',
    url = 'https://github.com/spacetelescope/stsci.numdisplay',
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'nose',
        'numpy',
        'sphinx',
        'stsci.sphinxext',
        'stsci.tools'
    ],
    package_dir = {
        '':'lib'
    },
    packages = find_packages(),
    package_data = {
        '': ['LICENSE.txt'],
        'stsci/numdisplay': [
            '*.dat',
            'imtoolrc'
        ]
    },
)
