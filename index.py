# DESENVOLVA UM PROGRAMA QUE O USUÁRIO IRÁ INFORMAR UMA PERGUNTA (UTILIZANDO EXATAMENTE AS PERGUNTAS DO QUESTIONÁRIO ANTERIOR E O SISTEMA DEVERÁ DAR A RESPOSTA.

# 1 - QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?
# 2 - QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?
# 3 - QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?
# 4 - COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?
# 5 - QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?
# 6 - QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?
# 7 - O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE. 

p1 = "QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO ?"
p2 = "QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO ?"
p3 = "QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO ?"
p4 = "COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA ?"
p5 = "QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA ?"
p6 = "QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR ?"
p7 = "O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR ?"

while True:
    pergunta = input("Digite uma pergunta: ")

    if pergunta == p1:
        print("Resposta: Joan tait")
    elif pergunta == p2:
        print("Resposta: Um computador quântico")
    elif pergunta == p3:
        print("Resposta: Streambarry")
    elif pergunta == p4:
        print("Resposta: Assistindo TV com o namorado Cris")
    elif pergunta == p5:
        print("Resposta: Joan entra em desespero, após isso procura uma forma de cancelar a série")
    elif pergunta == p6:
        print("Resposta: Ignorância ao aceitar termos e condições, além do assustador avanço da técnologia.")
    elif pergunta == p7:
        print("Resposta: Não tenho certeza, pois não conheço a serie.")
    else:
        print("Não tenho resposta pra esse pergunta, tente novamente")
    
    