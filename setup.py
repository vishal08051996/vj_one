from setuptools import find_packages,setup

hyphen_e = "-e ."


def get_requirements(file_path):
    """
    function given the file path of require packages with return list of packages
    """

    with open(file_path) as file_obj:
        packages = file_obj.readlines()
        packages = [i.replace("\n","") for i in packages]
        if hyphen_e in packages:
            packages.remove(hyphen_e)

    return packages



setup(
    name="machine learning",
    version="0.001",
    author="vishal",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)