import telepot
bot = telepot.Bot("token")

Chat_id = bot.getUpdates()[0]['message']['chat']['id']

menu = ["Olá, como posso ajudá-l@? Escolha uma opção pelo seu número:", [], []]
menu[1] = ["1 - Desejo adquirir o cartão Carrefour.", [], []]
menu[2] = ["2 - Já possuo o cartão Carrefour.", [], []]
menu[1][1] = ["1 - Desejo adquirir um cartão de débito.", "Por favor, preencha o formulário para requerer seu cartão de débito: https://forms.gle/s4u96EeK5y98vgxL6. Digite 0 para volta ao menu inicial ou qualquer outro número para encerrar nossa conversa."]
menu[1][2] = ["2 - Desejo adquirir um cartão de crédito.", "Por favor, preencha o formulário para requerer seu cartão de créditod: https://forms.gle/hABsXSCJv2Q5kcJF9. Digite 0 para volta ao menu inicial ou qualquer outro número para encerrar nossa conversa."]
menu[2][1] = ["1 - Desejo conferir meu extrato.", "Seu extrato: https://drive.google.com/file/d/1eYUNtfHwWPKFGbsJzgn4bEGVkVjrnTWg/view?usp=sharing. Digite 0 para volta ao menu inicial ou qualquer outro número para encerrar nossa conversa."]
menu[2][2] = ["2 - Desejo obter minha fatura do mês corrente.", "Sua fatura:https://drive.google.com/file/d/14hLvAUjRwaqfTjW1OeuV4lC_yFmN7_KB/view?usp=sharing.  Digite 0 para volta ao menu inicial ou qualquer outro número para encerrar nossa conversa."]

Antes = 1
zero = ''
opcao = [0,0]
while True:
	
	while Antes > 1:
		zero = bot.getUpdates()[len(bot.getUpdates()) - 1]['message']['text']
		if zero == '0':
			break
	bot.sendMessage(Chat_id,menu[0])
	bot.sendMessage(Chat_id,menu[1][0])
	bot.sendMessage(Chat_id,menu[2][0])	

	Antes = len(bot.getUpdates())
	Depois = len(bot.getUpdates())

	while Antes == Depois:
		Depois = len(bot.getUpdates())

	Indice = Depois - 1
	Resposta = bot.getUpdates()[Indice]['message']['text']
	opcao[0] = int(Resposta)

	bot.sendMessage(Chat_id,menu[opcao[0]][1][0])
	bot.sendMessage(Chat_id,menu[opcao[0]][2][0])

	Antes = Depois
	while Antes == Depois:
		Depois = len(bot.getUpdates())

	Indice = Depois - 1
	Resposta = bot.getUpdates()[Indice]['message']['text']
	opcao[1] = int(Resposta)

	bot.sendMessage(Chat_id,menu[opcao[0]][opcao[1]][1])

	Antes = Depois
	while Antes == Depois:
		Depois = len(bot.getUpdates())
	
	Indice = Depois - 1
	Resposta = bot.getUpdates()[Indice]['message']['text']

	Antes = int(Resposta) + 1

	if Antes != 1 :
		bot.sendMessage(Chat_id,'Obrigad@ por usar os serviços do Banco Carrefour! Se quiser retornar a conversa digite 0.')
