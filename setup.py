from setuptools import find_packages, setup


setup(
    name='python-bible',
    version='0.1',
    py_modules=['bible'],
    package_dir={'bible': 'bible'},
    packages=find_packages(),
    include_package_data=True,
)
