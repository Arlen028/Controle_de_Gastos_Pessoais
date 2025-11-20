
print("=== CONTROLE DE GASTOS PESSOAIS ===")
print()

quantidade_despesas = int(input("Quantas despesas você deseja registrar? "))

total_gasto = 0.0
maior_valor = 0.0
nome_maior_despesa = ""
despesas = []

for i in range(quantidade_despesas):
    print(f"\nDespesa {i + 1}:")
    nome_despesa = input("Nome da despesa: ")
    valor_despesa = float(input("Valor R$ "))
    
    total_gasto += valor_despesa
    
    despesas.append({"nome": nome_despesa, "valor": valor_despesa})
    
    if valor_despesa > maior_valor:
        maior_valor = valor_despesa
        nome_maior_despesa = nome_despesa

media_gasto = total_gasto / quantidade_despesas

print("\n" + "="*50)
print("          RESUMO MENSAL")
print("="*50)
print(f"Total de despesas registradas: {quantidade_despesas}")
print(f"Total gasto no mês: R$ {total_gasto:.2f}")
print(f"Média dos gastos: R$ {media_gasto:.2f}")
print(f"Maior despesa: {nome_maior_despesa} - R$ {maior_valor:.2f}")
print("="*50)

print("\n--- LISTA DE TODAS AS DESPESAS ---")
for i, despesa in enumerate(despesas, 1):
    print(f"{i}. {despesa['nome']}: R$ {despesa['valor']:.2f}")