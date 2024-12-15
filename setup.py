from setuptools import setup, find_packages

setup(
    name="automation-framework",
    version="0.1.0",
    author="Isleimar Oliveira",
    author_email="isleimar@gmail.com",
    description="foo",
    long_description=open('docs/README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/isleimar/automation_framework",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=[
        "selenium>=4.0.0",
        "requests>=2.26.0",
        "pyyaml>=5.4",
    ],
    extras_require={
        "dev": ["pytest>=6.2.5"],
    },
    entry_points={
        "console_scripts": [
            "automation-framework=automation.core:main",
        ]
    },
    include_package_data=True,
)
