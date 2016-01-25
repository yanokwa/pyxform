from setuptools import setup, find_packages

setup(
    name='pyxform',
    version='0.9.22',
    author='modilabs',
    author_email='info@modilabs.org',
    packages=find_packages(),
    package_data={
        'pyxform.odk_validate': [
            'ODK_Validate.jar',
        ],
        'pyxform.tests': [
            'example_xls/*.*',
            'bug_example_xls/*.*',
            'test_output/*.*',
            'test_expected_output/*.*',
        ]
    },
    url='http://pypi.python.org/pypi/pyxform/',
    description='A Python package to create XForms for ODK Collect.',
    long_description=open('README.rst', 'rt').read(),
    install_requires=[
        'xlrd==0.8.0',
        'lxml==2.3.4',
    ],
)
