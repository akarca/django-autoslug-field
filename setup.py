#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-autoslug-field',
    version='0.2.3',
    description="AutoSlugField for Django based on django-extensions AutoSlugField, adds option to track foreignkey/parent field for slug.",
    long_description=open('README.rst').read(),
    author='Serdar Akarca',
    author_email='serdar@yuix.org',
    url='http://github.com/serdarakarca/django-categories',
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    keywords="django autoslug slug field",
    platforms=['any'],
)
