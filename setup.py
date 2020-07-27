from setuptools import setup, find_packages


def get_dependencies():
    deps = None
    with open("dependencies.txt", "r") as deps:
        deps = tuple(map(lambda dep: dep.strip(), deps.readlines()))

    return deps


setup(
    name="EmaratHolidays Testing Framework",
    version="1.0.0",
    author="Alex",
    author_email="a.hornovych@gmail.com",
    packages=find_packages(),
    install_requires=get_dependencies()
)
