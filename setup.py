from setuptools import setup


setup(
    name="aocd",
    version="0.1",
    description="dummy name to pull advent-of-code-data",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author="Wim Glenn",
    author_email="hey@wimglenn.com",
    license="MIT",
    url="https://github.com/wimglenn/aocd",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=["advent-of-code-data"],
    options={"bdist_wheel": {"universal": "1"}},
)
