
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Summary

Attributes:
    dev_reqs (TYPE): Description
    install_reqs (TYPE): Description
"""

from setuptools import setup
from setuptools import setup, find_packages


def parse_requirements(filename):
    """load requirements from a pip requirements file 

    Args:
        filename (TYPE): Description

    Returns:
        TYPE: Description
    """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


install_reqs = reqs = parse_requirements('requirements.txt')
dev_reqs = parse_requirements("requirements_dev.txt")

setup(
    name='pypolicescanner',
    version='0.1.0',
    description="Use RTL-SDR to scan the police frequencies",
    long_description="TODO: Fill in",
    author="Kevin Wierman",
    author_email='kwierman@gmail.com',
    url='https://github.com/kwierman/pypolicescanner',
    packages=find_packages(),
    package_dir={'pypolicescanner':
                 'pypolicescanner'},
    entry_points={
        'console_scripts': [
            'pypolicescanner=pypolicescanner.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=reqs,
    license="MIT license",
    zip_safe=False,
    keywords='pypolicescanner',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=dev_reqs
)
