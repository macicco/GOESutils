#!/usr/bin/env python
install_requires = ['python-dateutil','numpy','imageio','scikit-image']
tests_require = ['nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='GOES_quickplot',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/goes-quick-plot',
      long_description=open('README.rst').read(),
      description='easily download and plot GOES weather satellite data',
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require,
                      'plots':['cartopy','matplotlib'],},
      python_requires='>=3.6',
	  )
