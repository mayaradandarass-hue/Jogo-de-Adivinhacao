import random
import time

print("\n\n")
print("                 .,,uod8B8bou,,.                             \n") 
print("              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.                    \n") 
print("         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||                   \n") 
print("         !...:!TVBBBRPFT||||||||||!!^^""'     ||||                   \n") 
print("         !.......:!?|||||!!^^""'              ||||                   \n")
print("         !.........||||                     ||||                   \n")
print("         !.........||||  ##                 ||||     ************************************              \n")
print("         !.........||||                     ||||     * Bem-Vindo ao jogo de Adivinhação *              \n")
print("         !.........||||                     ||||     ************************************              \n")
print("         !.........||||                     ||||                   \n")
print("         !.........||||                     ||||                   \n")
print("         `.........||||                    ,||||                   \n")
print("          .;.......||||               _.-!!|||||                   \n")
print("   .,uodWBBBBb.....||||       _.-!!|||||||||!:'                    \n")
print("!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....               \n")
print("!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.             \n")
print("!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.           \n")
print("!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"";:::       `.         \n")
print("!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.   \n")
print("`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo. \n")
print("  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'\n")
print("    `........::::::::::::::::;iof688888888888888888888b.     `     \n")
print("      `......:::::::::;iof688888888888888888888888888888b.         \n")
print("        `....:::;iof688888888888888888888888888888888899fT!        \n")
print("          `..::!8888888888888888888888888888888899fT|!^""          \n")
print("            `' !!988888888888888888888888899fT|!^""                \n")
print("                `!!8888888888888888899fT|!^""                      \n")
print("                  `!988888888899fT|!^""                            \n")
print("                    `!9899fT|!^""                                  \n")
print('\n')

i = None
chute = None
pontos = 1000
acertou = False
intervalo1 = None
intervalo2 = None
tentativas = None
ultimo_numero = None
nivel = ("(1)Fácil (2)Médio (3)Difícil")
jogarnovamente = ("(1) Para jogar novamente (2) Para sair")


a = abs(-10)
b = abs(10)
x = 10
y = abs(x)


while True:
    acertou = False
    pontos = 1000 
    nivel = ("(1)Fácil (2)Médio (3)Difícil")

    print("\nEscolha o intervalo em que você deseja adivinhar o número secreto.\n")
    intervalo1 = int(input("Intervalo 1: "))
    intervalo2 = int(input("Intervalo 2: "))

    print('Escolha um nível de dificuldade.\n')
    print(nivel)
    nivel = int(input("\nDigite: "))

    if (nivel == 1):
        tentativas = 15
    elif(nivel == 2):
        tentativas = 10
    elif (nivel == 3):
        tentativas = 5
    

    min = intervalo1 if intervalo1 < intervalo2 else intervalo2
    max = intervalo2 if intervalo2 > intervalo1 else intervalo1
    
    numerosecreto = random.randint(min, max)

    while numerosecreto == ultimo_numero: 
        numerosecreto = random.randint(min, max) 
    ultimo_numero = numerosecreto
    
    tentativas_validas = 0

    for i in range(1, tentativas + 1):
        while True:
            print(f"\n{tentativas_validas + 1}º tentativa de {tentativas}\n")
            chute = int(input(f"Digite seu chute: "))

            if chute < 0:
                print("\nVocê não pode digitar números negativos.\n")
                continue

            if chute < min or chute > max:
                print(f"\nVocê deve digitar um número entre {min} e {max}!\n")
                continue
            
            tentativas_validas += 1
            break

        diferenca = abs(chute - numerosecreto)

        if chute == numerosecreto:
            acertou = True
            print("                          MM                      \n")
            print("                        MM##                      \n")
            print("                        ####mm                    \n")
            print("                      MM######                    \n")
            print("                      ########mm                  \n")
            print("                    mm##########                  \n")
            print("                    ############mm                \n")
            print("                  MM##############..              \n")
            print("    ::########################################@@..\n")
            print("    ############################################@@ \n")
            print("      ########################################@@  \n")
            print("        ####################################@@    \n")
            print("          ################################MM      \n")
            print("            ############################MM     🎉 Você acertou o número secreto!   \n")
            print(f"              ########################MM       Você fez {pontos} pontos   \n")
            print("              ########################MM          \n")
            print("              ##########################          \n")
            print("              ##########################          \n")
            print("            MM##########################          \n")
            print("            ############mm  ############          \n")
            print("            ########MM          ########          \n")
            print("            ######                ..####mm        \n")
            print("            ##                        --##        \n")
            break

        elif diferenca <= 3:
            print("\n🔥Muito quente! Você está colado nele!")

        elif diferenca <= 6:
            print("\n✨Quente! Você está perto!")

        else:
            print("\n❄️ Frio... Você está longe de acertar.")

        pontosperdidos = abs(chute - numerosecreto)/2.0
        pontos = pontos - pontosperdidos

        print("\n")
    
    if not acertou:
        print("\n")
        print('                         __    _                           \n')    
        print('                    _wr""        "-q__                     \n')
        print('                 _dP                 9m_                   \n')
        print('               _#P                     9#_                 \n')
        print('              d#@                       9#m                \n') 
        print('             d##                         ###               \n')
        print('            J###                         ###L              \n')
        print('            {###K                       J###K              \n')
        print('            ]####K      ___aaa___      J####F              \n')
        print('        __gmM######_  w#P""   ""9#m  _d#####Mmw__          Você perdeu! Tente novamente!\n')
        print(f'     _g##############mZ_         __g##############m_        O número secreto era: {numerosecreto}\n')
        print('   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_     \n')
        print('  a###""          ,Z"#####@" "######"g,          ""M##m    \n')
        print(' J#@"             0L  "*##     ##@"  J#              *#K   \n')
        print(' #"               `#    "_gmwgm_~    dF               `#_  \n')
        print('7F                 "#_   ]#####F   _dK                 JE  \n')
        print(']                    *m__ ##### __g@"                   F  \n')
        print('                       "PJ#####LP"                         \n')
        print(' `                       0######_                      ´   \n')
        print('                       _0########_                         \n')
        print('     .               _d#####^#####m__              ,       \n')
        print('      "*w_________am#####P"   ~9#####mw_________w*"        \n')
        print('          ""9@#####@M""           ""P@#####@M""            \n')
        print('\n')
    
    print(f"Digite (1) Para jogar novamente ou (2)Para sair")
    jogarnovamente = int(input("Digite: "))

    if jogarnovamente == 2:
        print("Obrigada por jogar!")
        break

#The End!





