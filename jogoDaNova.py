class JogoDaVelha:
    def __init__(self):
        self.__tabuleiro = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.__tabu_tela = ['_',' ',' ',' ',' ',' ',' ',' ',' ']
        self.__tabu_var = [1,0,0,0,0,0,0,0,0]
        self.__turnox = True
        self.__executando = True
        self.__posicoes_vitoria = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.__jogo_string = """
 {0} | {1} | {2}
---|---|--- 
 {3} | {4} | {5}
---|---|--- 
 {6} | {7} | {8}
"""

    @property
    def turnox(self):
        return self.__turnox

    @property
    def executando(self):
        return self.__executando

    @property
    def jogo_string(self):
        return self.__jogo_string

    @property
    def tabuleiro(self):
        return self.__tabuleiro

    @property
    def tabu_tela(self):
        return self.__tabu_tela

    @property
    def tabu_var(self):
        return self.__tabu_var

    @property
    def posicoes_vitoria(self):
        return self.__posicoes_vitoria

    
    def altera_turno(self):
        self.__turnox = not self.__turnox

    def para_execucao(self):
        self.__executando = False



    def mostra_jogo(self):
        print(self.__jogo_string.format(*self.__tabu_tela))
    
    def mostra_jogo_sem_cursor(self):
        print(self.__jogo_string.format(*self.tabuleiro))


    def executar(self):
        while self.__executando:
            self.mostra_jogo()
            opcao = input('Digite o que deseja fazer\n1 - Avancar\n2 - Retroceder\n3 - Selecionar\nOutro - Sair\n')
            
            if opcao == '1': self.avancar()
            elif opcao == '2': self.retroceder()
            elif opcao == '3': self.selecionar()
            else: self.para_execucao()
    

    
    def avancar(self):
        condicao = True
        index = self.__tabu_var.index(1)
        posicao = index
        self.__tabu_var[index] = 0
        self.__tabu_tela[index] = self.__tabuleiro[index]

        while condicao:
            if posicao == len(self.__tabu_var) - 1: posicao = 0
            else: posicao += 1
            if self.__tabuleiro[posicao] == ' ': condicao = False
            
        self.__tabu_var[posicao] = 1
        self.__tabu_tela[posicao] = '_'



    def retroceder(self):
        condicao = True
        index = self.__tabu_var.index(1)
        posicao = index
        self.__tabu_var[index] = 0
        self.__tabu_tela[index] = self.__tabuleiro[index]

        while condicao:
            if posicao == 0: posicao = len(self.__tabu_var) - 1
            else: posicao -= 1
            if self.__tabuleiro[posicao] == ' ': condicao = False
            
        self.__tabu_var[posicao] = 1
        self.__tabu_tela[posicao] = '_'



    def selecionar(self):
        condicao = True

        if self.turnox:
            caractere = 'X'
        else:
            caractere = 'O'

        index = self.__tabu_var.index(1)
        posicao = index

        self.__tabuleiro[index] = caractere
        self.__tabu_tela[index] = caractere

        self.__tabu_var[index] = 0


        contador = 1
        while condicao:
            if posicao == len(self.__tabu_var) - 1: posicao = 0
            else: posicao += 1
            if self.__tabuleiro[posicao] == ' ': condicao = False
            if contador > 9:
                self.deuVelha()
                return
            contador += 1

        self.__tabu_var[posicao] = 1
        self.__tabu_tela[posicao] = '_'

        self.valida_casas()
        self.altera_turno()



    def deuVelha(self):
        self.para_execucao()
        print('\n----------------------\nDeu velha lkkkkkkkkkkk\n----------------------\n')
        self.mostra_jogo_sem_cursor()


    def vitoria(self, caractere):
        self.para_execucao()
        print(f'\n----------------------------\nParabéns, o {caractere} foi o vencedor\n----------------------------\n')
        self.mostra_jogo_sem_cursor()


    def valida_casas(self):
        for posicao in self.posicoes_vitoria:
            self.valida_linha(posicao, 'X')
            self.valida_linha(posicao, 'O')


    def valida_linha(self, posicao, caractere):
        if self.tabuleiro[posicao[0]] == self.tabuleiro[posicao[1]] == self.tabuleiro[posicao[2]] == caractere:
            self.vitoria(caractere)


# --------------------------------------------------------------------- made by Ângelo

jogo = JogoDaVelha()
jogo.executar()