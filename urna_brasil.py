from src.application.config import NUMEROS_REPETICOES
def votacao(candidato):  # fução para votação com a variavel candidato como argumento
    global  candidato_bolsonaro,candidato_lula, candidato_siro,candidato_manuel,voto_nulo,voto_em_branco
 
    if candidato.isalpha():  # checa se candidato contem apenas letras
        if candidato == 'Fim' or candidato == 'fim' or candidato == 'FIM':
            print('FIM DA VOTAÇÃO')
            print_resultados()

    elif candidato.isnumeric():  # checa se candidato e um caracter numerico
        if candidato == '1' or candidato == '2' or candidato == '3'or candidato == '4'or candidato == '5' or candidato =='6':
            if candidato == '1':
                candidato_bolsonaro += 1
            elif candidato == '2':
                 candidato_lula += 1
            elif candidato == '3':
                 candidato_siro += 1
            elif candidato == '4':
                 candidato_manuel += 1
            elif candidato == '5':
                 votu_nulo += 1
            elif candidato == '6':
                 votu_EM_BRANCO += 1
        else:  # se o valor digitado nao e valido, há entrada de novo candidato e a funcao repete
            candidato= str(input('Digite um numero valido para o candidato: '))
            votacao(candidato)


def print_resultados():  # printa resultados e encerra programa
    global  candidato_bolsonaro,candidato_lula, candidato_siro,candidato_manuel,voto_nulo,voto_em_branco

    print('QUANTIDADE DE VOTOS:\n')
    print('CANDIDATO JOSÉ DA SILVA - TOTAL DE ' + str(candidato_bolsonaro))
    print('CANDIDATO MARIA DO JURUNAS - TOTAL DE ' + str(candidato_lula))
    print('CANDIDATO JOÃO DO TAPANÃ - TOTAL DE ' + str(candidato_siro))
    print('CANDIDATO JOÃO DO TAPANÃ - TOTAL DE ' + str(candidato_manuel))
    print('CANDIDATO JOÃO DO TAPANÃ - TOTAL DE ' + str(voto_nulo))
    print('CANDIDATO JOÃO DO TAPANÃ - TOTAL DE ' + str(voto_em_branco))

    exit()  # encerra prog


if __name__ == '__main__':  # funcao main 
    candidato_lula = 0
    candidato_bolsonaro = 0
    candidato_siro = 0
    candidato_manuel = 0
    voto_nulo = 0
    voto_em_branco = 0

    while True:  # laço ocorre indefinidamente ate que ocorra o 'Fim'
        candidato = str(input('ELEIÇÃO ESPECIAL\nDigite o numero do seu candidato: '))
        votacao(candidato)