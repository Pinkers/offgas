from setuptools import setup

GITHUB_URL = 'http://github.com/vfilimonov/co2meter'

exec(open('co2meter/_version.py').read())

# Long description to be published in PyPi
LONG_DESCRIPTION = """
**offgas** is a Python interface to the USB CO2 monitor with monitoring and
logging tools for fermentation.
"""

setup(name='offgas',
      version=__version__,
      description='Python interface to the USB CO2 monitor',
      long_description=LONG_DESCRIPTION,
      url=GITHUB_URL,
      download_url=GITHUB_URL + '/archive/v%s.zip' % (__version__),
      author='Aaron Kirby',
      author_email='aaronkirby2000@gmail.com',
      license='MIT License',
      packages=['co2meter'],
      install_requires=['hidapi', 'future', 'pandas'],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': ['co2meter_server = co2meter:start_server',
                              'co2meter_homekit = co2meter:start_homekit',
                              'co2meter_server_homekit = co2meter:start_server_homekit',
                              ],
      },
      classifiers=['Programming Language :: Python :: 3', ]
      )
