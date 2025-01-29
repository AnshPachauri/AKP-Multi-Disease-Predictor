from setuptools import find_packages,setup
from typing import List

def get_req(file_path:str)->List[str]:
    requirements=[]
    with open('requirements.txt') as my_requirements:
        requirements=my_requirements.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements=requirements.remove('-e .')

        return requirements

setup(
    name='Multi-Disease-Predictor',
    version='0.0.1',
    author='Ansh Kumar Pachauri',
    author_email='anshpachauri84@gmail.com',
    packages=find_packages(),
    install_requirements=get_req('requirements.txt')

)