import os

# 1. Criação da estrutura de diretórios
os.makedirs("meu_pacote", exist_ok=True)

# 2. Criando o arquivo __init__.py
init_content = '''\
# meu_pacote/__init__.py

from .meu_modulo import minha_funcao

__all__ = ['minha_funcao']
'''

with open("meu_pacote/__init__.py", "w") as f:
    f.write(init_content)

# 3. Criando o arquivo meu_modulo.py
modulo_content = '''\
# meu_pacote/meu_modulo.py

def minha_funcao():
    return "Olá, este é o meu pacote!"
'''

with open("meu_pacote/meu_modulo.py", "w") as f:
    f.write(modulo_content)

# 4. Criando o arquivo setup.py
setup_content = '''\
# setup.py

from setuptools import setup, find_packages

setup(
    name='meu_pacote',
    version='0.1',
    packages=find_packages(),
    description='Um pacote Python simples',
    author='Seu Nome',
    author_email='seu_email@example.com',
    url='https://github.com/seu_usuario/meu_pacote',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
'''

with open("setup.py", "w") as f:
    f.write(setup_content)

print("Pacote 'meu_pacote' criado com sucesso!")
