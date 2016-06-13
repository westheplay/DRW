#! /usr/bin/python
# -*- coding: utf-8
#Agenda de contatos -- Versão zero à esquerda!
#Aprendendo a programar -- Weslley Barros
import sys, shelve

try:
	inp = raw_input
	
except NameErro:
	inp = input
	
def registrar(bd, nome):
    #Função para registrar novos contatos no bando de dados
    fone=str(raw_input('\nDigite o telefone do novo contato: '))
    email=str(raw_input('\nDigite o endereço do correio eletrônico do novo contato: '))
    msn=str(raw_input('\nDigite o endereço de MSN do novo contato: '))
   
    fone=('fone', fone)
    email=('email', email)
    msn=('msn', msn)
    cadastro=fone, email, msn
    bd[nome]=dict(cadastro)
    #return
   
def mostrar(bd, nome):
    #Função para mostrar registros do banco de dados.
    print "\nFormas de contato com %s" %(nome)
    print "\nTelefone: " + bd[nome]['fone']
    print "Correio Eletrônico: " +bd[nome]['email']
    print "MSN: " +bd[nome]['msn']
    return

def alterar(bd, nome):
    #Função para alterar dados no banco de dados - Não funciona!!!
    retorno="sim"
    while retorno=="sim":
        alteracao=str(raw_input("Que informação gostaria de alterar? "))
        if alteracao=="telefone":
            fone=str(raw_input("Digite o novo número de telefone: "))
            fone={'fone': fone}
            bd[nome].update(fone)
        elif alteracao=="correio eletrônico":
            email=str(raw_input("Digite o novo endereço de correio eletrônico: "))
            bd[nome]['email']=email
        elif alteracao=='msn':
            msn=str(raw_input("Digite o novo endereço de MSN: "))
            bd[nome]['msn']=msn
        else:
            print "Opção inválida"
        retorno=str(raw_input("Gostaria de mudar mais alguma informação? "))
       
def apagar(bd):
    #Função para limpar banco de dados
    confirmar=str(raw_input("VOCÊ TEM CERTEZA QUE QUER APAGAR A LISTA *TODA*?? "))
    if confirmar=="sim":
        bd.clear()
    elif confirmar=='não':
        return
    else:
        print "Opção inválida!!"
        return
               
def principal():
    #Agora... juntando tudo!!
    bd=shelve.open('dados.db')   #Abrindo o banco de dados
    try:
        while 1:                        #Fica trampando até eu mandar parar!!
            nome=str(raw_input("Digite um nome, por favor: "))     
            if nome in bd:
                mostrar(bd, nome)
                alteracao=str(raw_input("Deseja fazer alteração no cadastro? "))
                if alteracao=="sim":
                    alterar(bd, nome)
                   
            elif nome not in bd and nome !="sair" and nome!="apagar":
                registro=str(raw_input("Nome não encontrado.\nDeseja cadastrar agora? "))
                if registro=="sim":
                    registrar(bd, nome)
            elif nome=="apagar":
                apagar(bd)
            elif nome=="sair":
                return
            else:
                print "Opção inválida!"
    finally:
        bd.close()         
#Colocando tudo pra funcionar.
principal()

