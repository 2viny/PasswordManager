import numpy as np
import random

class userInfo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accounts = dict()

    def getAccounts (self):
        return self.accounts()
    
    def getUsername (self):
        return self.username

    def lookUser (self):
        print(f"user: {self.username} \npassword: {self.password}")

class usersTable:
    def __init__ (self) :
        self.tableSize = 100
        self.users = [[] for i in range(self.tableSize)]

    def olhar(self):
        for i in range(self.tableSize):
            print(self.users[i])

    def hashIndex (self, username):
        index = 0
        for char in username:
            index += ord(char)
        return index % self.tableSize
    
    def getUser (self, search):       
        i = self.hashIndex(search)
        for registeredUser in self.users[i]:
            if registeredUser.getUsername() == search:
                return registeredUser
    
    def setUser (self, user):
        username = user.getUsername()
        i = self.hashIndex(username)
        found = False
        for j, registerUser in enumerate(self.users[i]):
            if registerUser.getUsername() == username:
                self.users[i][j] = (user)
                found = True
                break
        if found == False:
            self.users[i].append((user))
    
    def deleteUser (self, user): #users.deleteUser(user)
        username = user.getUsername()
        i = self.hashIndex(username)
        for j, registerUser in enumerate(self.users[i]):
            if registerUser.getUsername() == username:
                del self.users[i][j]
                break



users = usersTable()
while True:
    action = input("\nQue ação deseja realizar?\
                   \n\"Registrar\": Registra um novo usuário.\
                   \n\"Entrar\": Entra com um usuário existente.\
                   \n\"Sair\": Fecha o programa.\n").lower()
    
    if action == "sair":
        quit()
    
    elif action == "registrar":
        username = input("Informe um usuário: ")
        password = input("Informe uma senha: ")
        user = userInfo(username, password)
        users.setUser(user)
    
    elif action == "entrar":
        search = input("Informe seu usuário: ")
        user = users.getUser(search)
        if user != None:
            password = input("Informe sua senha: ")
            if password == user.password:
                print("Acesso garantido.")
                
                while True:
                    action = input("\nQue ação deseja realizar?\
                                    \n\"Ler\": Ver suas contas.\
                                    \n\"Adicionar\": Adiciona uma nova conta.\
                                    \n\"Remover\": Remove uma conta existente.\
                                    \n\"Apagar\": Apaga seu usuário.\
                                    \n\"Sair\": Sai do seu usuário e renorna ao início.\n").lower()
                    if action == "ler":
                        for plataform, plataformPassword in user.accounts.items():
                            print(f"{plataform}: {plataformPassword}")
                    if action == "adicionar":
                        plataform = input("Informe a plataforma: ")
                        plataformPassword = input("Informe a senha: ")
                        user.accounts[plataform] = plataformPassword
                    if action == "remover":
                        plataform = input("Informe a plataforma que deseja remover: ")
                        if plataform in user.accounts:
                            del user.accounts[plataform]
                        else:
                            print("Conta inexistente.")
                    if action == "apagar":
                        password = input("Informe sua senha para confirmar: ")
                        if password == user.password:
                            users.deleteUser(user)
                            print("Seu usuário foi deletado.")
                            break
                        else:
                            print("Senha incorreta.")
                    if action == "sair":
                        break
            else:
                print("Acesso negado.")
        
        else:
            print("Usuário inexistente.")
    
    elif action == "devtools":
        while True:
            action = input("\nEstá é uma ferramenta para testes, que função deseja realizar?\
                            \n\"Gerar\": Gera alguma quantidade de usuários aleatórios.\
                            \n\"Vizualizar\": Vizualiza todos os usuários existentes.\
                            \n\"Sair\": Sai das ferramentas de testes e renorna ao início.\n").lower()

            if action == "sair":
                break

            if action == "gerar":
                lower_abc = "abcdefghijklmnopqrstuvwxyz"
                upper_ABC = lower_abc.upper()
                letters = lower_abc + upper_ABC
                generatedUsers = int(input("Quantos usuários aleatórios você deseja gerar? "))
                for i in range(generatedUsers):
                    username = "".join(random.sample(letters, random.randint(3, 8)))
                    user = userInfo(username, "randomUser")
                    users.setUser(user)
            
            if action == "vizualizar":
                users.olhar()