import re

print("=== VALIDADOR ===")
telefone = input("Digite um telefone (Ex: 91 91234-5678): ")

valido_telefone = re.match(r'^\d{2} \d{5}-\d{4}$', telefone) is not None

print("\nResultados:")

if (valido_telefone == True) :
    print("Telefone Válido!")
else:
    print("Telefone Inválido!")


# T → \d{2} \d{5}-\d{4}  
# \d = [0-9]

