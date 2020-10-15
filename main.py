from operacao_banco import Operacoes
import psycopg2

op = Operacoes()
autor = str(input("Digite o autor"))
tipo = str(input("Digite o tipo"))
op.salvar(autor, tipo)
op.buscar()