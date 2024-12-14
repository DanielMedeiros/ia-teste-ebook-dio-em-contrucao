import pandas as pd
import random
from datetime import datetime, timedelta

# Definir os valores possíveis para cada coluna
tipos = ["ENTRADA", "SAÍDA"]
categorias = ["RENDA FIXA", "ALIMENTAÇÃO", "TRANSPORTE", "LAZER", "SAÚDE", "EDUCAÇÃO"]
descricoes = ["Salário Mensal", "Compras no Mercado", "Gasolina", "Cinema", "Consulta", "Curso"]
operacoes_bancarias = ["TRANSFERÊNCIA", "CRÉDITO", "DÉBITO"]
status = ["RECEBIDO", "PENDENTE", "PAGO"]

# Gerar 30 linhas de dados
num_linhas = 30
data_inicial = datetime(2023, 1, 1)
data_final = datetime(2023, 12, 31)
dados = []

for _ in range(num_linhas):
    linha = {
        "Data": (data_inicial + timedelta(days=random.randint(0, (data_final - data_inicial).days))).strftime("%Y-%m-%d"),
        "Tipo": random.choice(tipos),
        "Categoria": random.choice(categorias),
        "Descrição": random.choice(descricoes),
        "Valor": round(random.uniform(10.0, 10000.0), 2),  # Valores entre 10 e 10.000
        "Operação Bancária": random.choice(operacoes_bancarias),
        "Status": random.choice(status)        
    }
    dados.append(linha)

# Criar o DataFrame
df = pd.DataFrame(dados)

# Salvar o DataFrame em um arquivo Excel
file_path = r"C:\Users\kabal\OneDrive\Documentos\IA\Python_gera_dados\massa_dados.xlsx"
df.to_excel(file_path, index=False)
