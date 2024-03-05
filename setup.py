from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

if __name__ == '__main__':
    setup(
        maintainer='Luke Davis',
        maintainer_email='lukelbd@gmail.com',
        description='A succinct matplotlib wrapper for making beautiful graphics.',
        install_requires=install_requires,
        python_requires='>=3.6',
        packages=find_packages(),
        version='1.0.0',
        name='proplot',
        include_package_data=True,
    )
