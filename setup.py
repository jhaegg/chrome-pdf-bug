from setuptools import setup, find_packages


setup(
    name="chrome-pdf-bug",
    version="1.0.0",

    entry_points={
        'console_scripts': [
            'chrome-pdf-bug=app:main',
        ]
    },
    packages=find_packages(),
)
