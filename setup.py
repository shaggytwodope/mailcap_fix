import setuptools

setuptools.setup(
    name='mailcap_fix',
    version='0.1.0',
    description='A patched mailcap module that conforms to RFC 1524',
    long_description=open('README.rst').read(),
    url='https://github.com/michael-lazar/mailcap_fix',
    author='Michael Lazar',
    author_email='lazar.michael22@gmail.com',
    license='UNLICENSE',
    keywords='mailcap 1524',
    packages=['mailcap_fix'],
)