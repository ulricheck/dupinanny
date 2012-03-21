# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

packages=find_packages('src')


setup(
    name="dupinanny",
    version="0.1",
    install_requires=[
    ],
    zip_safe=False,
    packages=packages,
    package_dir = {'':'src'},
    keywords=[
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points = {
        'console_scripts': [
            'dupinanny = dupinanny.backup:start',
        ],
    },
    # Uncomment next line and create a default.cfg file in your project dir
    # if you want to package a default configuration in your egg.
    #data_files = [('config', ['default.cfg'])],
    )
