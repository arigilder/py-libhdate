#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = "Royi Reshef"
__maintainer__ = "Tsvi Mostovicz"
__version__ = "0.8.7"

from codecs import open
from os.path import abspath, dirname, join

from setuptools import setup

here = abspath(dirname(__file__))

# Get the long description from the README file
with open(join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='hdate',
      version=__version__,
      description='Hebrew date and Zmanim',
      long_description=long_description,
      url='https://github.com/royi1000/py-libhdate',
      classifiers=[
           'Development Status :: 5 - Production/Stable',
           'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',  # noqa: E501
           'Programming Language :: Python :: 2.7',
           'Programming Language :: Python :: 3'
      ],

      author=__author__,
      author_email='roy.myapp@gmail.com',
      maintainer=__maintainer__,
      maintainer_email='ttmost@gmail.com',
      license='GPLv3+',
      packages=['hdate'],
      install_requires=[
          'python-dateutil',
          'six'
      ],
      extras_require={
        'dev': ['tox'],
        'pub': ['bumpversion', 'wheel', 'twine']
      },
      python_requires='>=2.7'
      )
