from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='connector.scripts',
      version=version,
      description="Odoo connector usefull recipe startup script",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Simon ANDRE',
      author_email='sandre@anybox.fr',
      url='anybox.fr',
      license='AGPL v3',
      namespace_packages=['connector'],
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'setuptools',
          'argparse',
      ],
      entry_points="""
      """
      )
