

venda = []

while True:
  entrada = input("Digite o nome do produto: ")

  if entrada == "fim":
    break

  venda.append(entrada)

print(f"registro finalizado. As vendas resgistradas são: {venda}")



#-----------------------------------------------------------------




vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50

print("Vendedores que bateram a meta de 50 vendas:")

i = 0
while i < len(vendas):
    if vendas[i] >= meta:
        print(f"{vendedores[i]} - Vendas: {vendas[i]}")
    i += 1
