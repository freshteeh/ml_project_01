from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="e ."

def get_requirememnts(file_path:str)->List[str]:
    '''
    this fuction will return the list of requirements
    '''
    requirement=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
 
setup(
    name="ml_project_01",
    version="0.0.1",
    author="Fereshta",
    author_email="fereshtamohammadbaqir@gmail.com",
    packages=find_packages(),
    install_requires=get_requirememnts("requirements.txt")
)