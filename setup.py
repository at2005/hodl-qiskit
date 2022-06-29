from setuptools import setup, find_packages

setup(
    name='hodl-qiskit',
    version='1.0.0',    
    description='A Qiskit Python package to call HODL inline',
    url='https://github.com/at2005/hodl-qiskit',
    author='Ayush Tambde',
    author_email='tambdeayush@gmail.com',
    license='MIT',
    packages=find_packages(),

    classifiers=[
        'Development Status :: Production',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',
	'Operating System :: MacOS'
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
