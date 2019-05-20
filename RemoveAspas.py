# Algoritmo python para remover aspas
# O campo arq.sql deve ser subistituido para o nome do arquivo com as aspas
# O campo novo.sql é o nome do arquivo que ira ser criado apos a remocao das aspas

with open(r'arq.sql', 'r') as infile, \
     open(r'novo.sql', 'w') as outfile:
    data = infile.read()
    data = data.replace('"', "")
    outfile.write(data)
