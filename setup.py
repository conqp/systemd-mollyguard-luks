#! /usr/bin/env python3
"""Install script."""


from distutils.core import setup


setup(
    name='mollyguardctl',
    version='latest',
    author='Richard Neumann',
    author_email='<mail at richard dash neumann period de>',
    maintainer='Richard Neumann',
    maintainer_email='<mail at richard dash neumann period de>',
    py_modules=['mollyguardctl'],
    scripts=['files/mollyguardctl'],
    description=('Mollyguards your system.'))