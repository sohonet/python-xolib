from setuptools import setup

setup(
    name='xolib',
    version='0.3.0',
    author='Vyronas Tsingaras',
    author_email='vyronas@vtsingaras.me',
    packages=['xolib'],
    url='https://github.com/vtsingaras/python-xolib',
    license='LICENSE.txt',
    description='Helper library for interfacing with xo-server.',
    long_description=open('README.rst').read(),
    install_requires=[
        "websocket-client",
        "six",
    ],
)
