#------------------------------------------------------------------------------------------------------------------------
# chat_gpt_api.py - Comunicação com a API do chat GPT
#------------------------------------------------------------------------------------------------------------------------
# Importa o pacote 
import openai as gpt 

api_chat_gpt_key = '<INSIRA SUA CHAVE AQUI>'
gpt.api_key = api_chat_gpt_key

print('*'*100)
print('\nSTARTING IN CHAT GPT\n')
print('*'*100)
print('\n')
print('Orientações:')
print('Caso deseja sair informe ao programa ao final de cada pergunta')
print('O modelo está calibrado para ter pequenas variações nas respostas')
print();

execution = True
answers_false = ['sair','não','out','no','exit','leave','nao']

while execution:
    print(f'CASO DESEJA PARA DIGITE {answers_false}')
    
    question = input('Input a text: ')

    if question in answers_false:
        print('Opções possíves')
        print(answers_false)

        answer_confirmation = input('Você ainda quer continuar?')
        
        if answer_confirmation in answers_false:
            break 
        else:
            continue
    
    question_user = gpt.Completion.create(
      engine='text-davinci-003',  # Motor de geração de texto
      prompt=question,
      max_tokens=50,  # Número máximo de tokens na resposta
      n=1,  # Número de respostas a serem geradas
      stop=None,  # Condição de parada para a resposta
      temperature=0.7  # Controla a aleatoriedade da resposta (0.0 a 1.0)
    )

    reply = question_user.choices[0].text.strip()

    print(f'\n{reply}')

    print('\n')
