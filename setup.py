from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of packages.
    """
    requirements=[]
    element_to_remove = "-e ."
    with open(file_path) as file:
        requirements = file.readlines()
        [req.replace ('\n',"") for req in requirements]
        
        if element_to_remove in requirements:
            requirements.remove(element_to_remove)
       
        return requirements
    
setup(
    name="MLproject",
    version="0.0.1",
    author="TharcisioS",
    autohor_email="tharcisiosouza.eng@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

