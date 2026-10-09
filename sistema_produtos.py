produtos = []

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    categoria = input("Categoria: ")

    produtos.append([nome, preco, categoria])

    resp = input("Deseja continuar? (s/n): ")
    if resp == "n":
        break

precos = []
categorias = []

for p in produtos:
    precos.append(p[1])
    categorias.append(p[2])

menor = min(precos)
maior = max(precos)
media = sum(precos) / len(precos)
estatisticas = (menor, maior, media)

categorias_unicas = set(categorias)

produtos_crescente = list(produtos)
produtos_crescente.sort(key=lambda x: x[1])

produtos_decrescente = sorted(produtos, key=lambda x: x[1], reverse=True)

limite = float(input("\nDigite um valor para filtrar: R$ "))

acima = []
abaixo = []

for p in produtos:
    if p[1] > limite:
        acima.append(p)
    if p[1] < limite:
        abaixo.append(p)

print("\n--- RELATÓRIO FINAL ---")
print(f"Menor preço: R$ {estatisticas[0]:.2f}")
print(f"Maior preço: R$ {estatisticas[1]:.2f}")
print(f"Média dos preços: R$ {estatisticas[2]:.2f}")

print("\nCategorias:")
for c in categorias_unicas:
    print(f"- {c}")

print("\nProdutos por preço crescente:")
for p in produtos_crescente:
    print(f"{p[0]} - R$ {p[1]:.2f} - {p[2]}")

print("\nProdutos por preço decrescente:")
for p in produtos_decrescente:
    print(f"{p[0]} - R$ {p[1]:.2f} - {p[2]}")

print(f"\nProdutos acima de R$ {limite:.2f}:")
for p in acima:
    print(f"{p[0]} - R$ {p[1]:.2f}")

print(f"\nProdutos abaixo de R$ {limite:.2f}:")
for p in abaixo:
    print(f"{p[0]} - R$ {p[1]:.2f}")