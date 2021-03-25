import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="comment-filter",
    version="0.0.1",
    author="Zhensu Sun",
    author_email="87su@tongji.edu.cn",
    description="A tool for fittering comments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/v587su/comment-filter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)