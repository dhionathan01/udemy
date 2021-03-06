from AcessarDados import (AcessarDados)
from AcessarDisco import (AcessarDisco)
from Departamento import (Departamento)
from Funcionario import (newFuncionario)
from Gerente import (Gerente)

funcionario = newFuncionario()
funcionario.set_id('01')
funcionario.set_nome('Dhionathan')
funcionario.set_matricula('332131551')
funcionario.set_departamento('Vendas')
funcionario.set_cargo('Vendedor')
funcionario.set_salario(3500.21)

AcessarDisco = AcessarDisco()
AcessarDados = AcessarDados()
AcessarDisco.salva(funcionario, 'funcionario')
AcessarDisco.escolher_arquivo('funcionario')
arquivo = AcessarDisco.abrir()
print(arquivo)

gerente = Gerente()
gerente.set_id('01')
gerente.set_departamento('Informatica')
gerente.set_matricula('321325')
gerente.set_cargo('Gerente')
gerente.set_nome('Dhionathan')
gerente.set_salario('5000')

AcessarDisco.salva(gerente, 'gerente')
AcessarDisco.escolher_arquivo('gerente')
arquivo = AcessarDisco.abrir()
print(arquivo)
print(type(arquivo))

departamento = Departamento()
departamento.set_id('01')
departamento.set_nome('Informatica')
departamento.set_gerente('Dhionathan')
departamento.abrir_caixa(100)
departamento.registar_venda(5, 50)
departamento.registar_venda(2, 30)
departamento.fechar_caixa()
AcessarDisco.salva(departamento, 'departamento')
AcessarDisco.escolher_arquivo('departamento')
arquivo = AcessarDisco.abrir()
print(arquivo)
