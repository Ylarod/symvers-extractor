#!/usr/bin/python3

from distutils.core import setup

setup(name='symvers-extractor',
      version='1.1',
      description='A tool to extractor symvers from a binary kernel',
      author='Ylarod',
      author_email='',
      url='https://github.com/Ylarod/symvers-extractor',
      install_requires=['vmlinux-to-elf @ git+https://github.com/marin-m/vmlinux-to-elf'],
      packages=[],
      scripts=['symvers_extractor', 'kallsyms_base']
     )
