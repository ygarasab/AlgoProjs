class Node:

    def __init__(self, valor):

        self.valor = valor
        self.pai = None
        self.filhos = []

        self.fa = None
        self.fb = None