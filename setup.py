from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="st-copy-to-clipboard-modified",
    version="0.1.7",
    author="Duke",
    author_email="ducanup0203@gmail.com",
    description="Streamlit component that allows you to copy text to the clipboard.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=["streamlit>=1.2", "jinja2"],
    url="https://github.com/ducanup01/st-copy-to-clipboard-modified",
)
