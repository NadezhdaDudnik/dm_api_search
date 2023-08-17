from distutils.core import setup

REQUIRES = [
    'grpc',
    'structlog',
    'google'
]

setup(
    name='dm_api_search',
    version='0.0.2',
    packages=['dm_api_search'],
    url='https://github.com/NadezhdaDudnik/dm_api_search.git',
    license='MIT',
    author='Nadezhda Dudnik',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_search with looger and gRPC'
)
