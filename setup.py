import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="retriever",
    version="0.0.1",
    description="Information finder",
    long_description=long_description,
    packages=setuptools.find_packages(),
)
