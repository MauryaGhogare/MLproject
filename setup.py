from setuptools import find_packages, setup
from typing import List

'''function to install requirements instead of installing them manually by mentioning
   each one like install_requires=['pandas','numpy'] in the setup func below'''
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]: 
    '''this func will return a list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n","") for req in requirements]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='MLproject',
    version='0.0.1',
    author='Maurya',
    author_email='mauryaghogare10@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)