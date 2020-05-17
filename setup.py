import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-turbolinks-elahmo",
    version="0.9.0",
    author="Ahmet Novalic",
    author_email="author@example.com",
    description="Turbolinks package for django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elahmo/django-turbolinks",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
