sexo = input("Olá, você é homem ou mulher? ")

if sexo == "mulher":
    i = "Sim"

    while i == "Sim":
        print("Bem-vinda!")
        print("MENU")
        print("Cadastro")
        print("Serviços")
        print("Ajuda")
        print("Sobre nós")
        print("Sair")

        opcao = input("Escolha sua opção: ")
        print("Você escoheu a opção: ", opcao)

        if opcao == "Cadastro":
            print("Se cadastre no nosso site para ter acesso a todos os nossos recursos para mulheres agricultoras")

            def cadastrar_usuario():

                usuario = input("Digite seu email ou nome de usuário: ")
                senha = input("Informe uma senha de acesso: ")
                cpf = input("Digite seu CPF: ")
                localidade = input("Informe sua cidade e estado: ")
                tel = input("Digite seu telefone com o DDD: ")

                print("\nCadastro realizado com sucesso!")
                print("Email: ", usuario)
                print("Senha: ", senha)
                print("CPF: ", cpf)
                print("Cidade: ", localidade)
                print("Telefone: ", tel)

            cadastrar_usuario()

        elif opcao == "Serviços":
            print("Escolha a sua área de preferência: ")
            print("(G)Grãos")
            print("(H)Horticultura")
            print("(A)Árvores frutíferas")

            area = input("Digite a opção escolhida: ").upper()[0]
            print("Você escolheu a área: ", area)

            grãos = ["Milho", "Trigo", "Arroz", "Soja"]
            horti = ["Batata", "Mandioca", "Alface", "Cenoura", "Brocólis"]
            arvores = ["Macieira", "Laranjeira",
                    "Jabuticabeira", "Bananeira", "Goiabeira"]

            if area == "G":
                print("Temos algumas opções de grãos para deixar sua plantação ainda mais variada:")
                print(grãos)

            elif area == "H":
                print("Temos algumas opções de legumes e verduras para você:")
                print(horti)

            elif area == "A":
                print("Temos algumas opções de sementes para as seguintes árvores frutíferas:")
                print(arvores)

        elif opcao == "Ajuda":
            print("CENTRAL DE AJUDA")
            duvida = input("Nos informe sua dúvida: ")
            print("Encaminharemos sua dúvida para o suporte técnico e logo entraremos em contato. Obrigada pela compreensão")

        elif opcao == "Sobre nós":
            print("A Solutech é uma empresa voltada para atender as necessidades de mulheres agricultoras que não possuem acesso a recursos produtivos e ao cooperativismo")

        elif opcao == "Sair":
            print("Saindo do menu...")
            print("Obrigado pela preferência e até logo!")
            
        resp = input("Deseja realizar outra opção? [Sim/Não]")
        i = resp
        
else:
    print("Desculpe, nossos serviços são voltados para mulheres agricultoras que sofrem com a desigualdade rural.")
