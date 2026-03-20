metros = float(input("Digite a distância em metros: "))
cm = metros * 100
mm = metros * 1000
print(f"{metros} m = {cm} cm = {mm} mm\n")

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))
novo_preco = preco - (preco * desconto / 100)
print(f"Preço com desconto: R${novo_preco:.2f}\n")

frase = input("Digite uma frase: ")
print(f"Quantidade de caracteres: {len(frase)}")
print(f"Tipo do dado: {type(frase)}\n")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
dias = idade * 365
print(f"Olá {nome}, você já viveu aproximadamente {dias} dias\n")

salario = float(input("Digite o salário: "))
novo_salario = salario * 1.15
print(f"Salário com aumento: R${novo_salario:.2f}\n")

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("Número par\n")
else:
    print("Número ímpar\n")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
print(f"Maior: {max(n1, n2, n3)}")
print(f"Menor: {min(n1, n2, n3)}\n")

num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

while True:
    senha = input("Digite a senha: ")
    if senha == "python123":
        print("Acesso Permitido\n")
        break
    else:
        print("Senha incorreta. Tente novamente.")

def estatisticas(lista):
    return max(lista), min(lista), sum(lista)

lista = []
for i in range(5):
    valor = float(input(f"Digite o {i+1}º número: "))
    lista.append(valor)

maior, menor, soma = estatisticas(lista)
print(f"Maior: {maior}, Menor: {menor}, Soma: {soma}\n")

produtos = {
    "arroz": 20.0,
    "feijao": 10.0,
    "macarrao": 5.0
}

busca = input("Digite o nome do produto: ").lower()
if busca in produtos:
    print(f"Preço: R${produtos[busca]:.2f}\n")
else:
    print("Produto não encontrado\n")

alunos = []

for i in range(3):
    print(f"\nCadastro do {i+1}º aluno:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    notas = []
    for j in range(3):
        nota = float(input(f"Nota {j+1}: "))
        notas.append(nota)
    
    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas
    }
    alunos.append(aluno)

print("\nMédias dos alunos:")
for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    print(f"{aluno['nome']} - Média: {media:.2f}")
