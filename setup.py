import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Brain-Tumor-MRI-Classification"
AUTHOR_USER_NAME = "kunalsingh1406"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "kunal964121@gmail.com"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Brain Tumor MRI Classification App built using python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kunalsingh1406/Brain-Tumor-MRI-Classification",
    project_urls={
        "Bug_Tracker": "https://github.com/kunalsingh1406/Brain-Tumor-MRI-Classification/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)