#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of DruPy.
# https://github.com/taylorpate/DruPy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Taylor Pate <taylorpate@gmail.com>

from setuptools import setup, find_packages
from DruPy import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='DruPy',
    version=__version__,
    description='Python module for accessing the Drupal Services API',
    long_description='''
Python module for accessing the Drupal Services API
''',
    keywords='Drupal Services API',
    author='Taylor Pate',
    author_email='taylorpate@gmail.com',
    url='https://github.com/taylorpate/DruPy',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'DruPy=DruPy.cli:main',
        ],
    },
)
