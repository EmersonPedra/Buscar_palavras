#  ---------------------------------------------------------------------------------------------------------------------
# Autor : Emerson Pedra
# Data : 28/11/2018
# Descriçao do programa: Analiza os arquivos existentes na pasta, procura pela palavra informada pelo usuario e cria um
# arquivo contendo as linhas que possuirem a palavra procurada
#  ---------------------------------------------------------------------------------------------------------------------

from os import listdir  # Importa o metodo listdir responsavel por listar os arquivos e diretorios da pasta
palavra = input('Informa a palavra procurada: \n')
nomes = listdir()  # Armazena os nomes dos arquivos presentes na pasta
novoarquivo = open('resultado.txt', 'w')  # Atualiza ou cria o arquivo com as linhas que tiverem a palavra procurada
for nome in nomes:  # Percorre a lista contendo o nome dos arquivos
    if nome[-4::1] == '.txt':  # Se a extensao do arquivo for txt executa o bloco de instruçoes a seguir
        try:
            arquivo = open(nome, 'r')  # Abre o arquivo para a analize
            tamanho = arquivo.seek(0, 2)  # Variavel que irá conter o indicador de fim do arquivo
            arquivo.seek(0, 0)  # Retorna o cursor pro inicio do arquivo
            numLinha = 0
            while True:
                linha = arquivo.readline()  # Lê uma linha do arquivo
                numLinha += 1  # Atualiza o contador de linhas
                novalinha = str(numLinha) + ' '
                if palavra in linha:  # Se a palavra procurada estiver na linha atual executa o bloco a seguir
                    novalinha += linha + ' '
                    novoarquivo.write(novalinha + '\n')
                if arquivo.tell() == tamanho:  # Se o cursor estiver no fim do arquivo op loop irá se incerrar
                    break
            arquivo.close()  # Fecha o arquivo que estava sendo analizado
        except IOError:
            print('Nao foi possivel abrir o arquivo {}'.format(nome))
novoarquivo.close()  # Fecha o arquivo que irá conter as linhas que tiverem a palavra procurada
