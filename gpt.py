import openai

openai.api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

messages = []
sys_msg = input("Enter The Type Of Assistant:\n")
messages.append({'role':'system','content':sys_msg})
print("\nYOUR ASSISTANT IS HERE!")

while input() != 'quit()':
    message= input('Enter Your question:')
    messages.append({'role':'user','content':message})
    response = openai.ChatCompletion.create(model = 'gpt-3.5-turbo',
                                            messages = messages)
    reply = response['choices'][0]['message']['content']
    messages.append({'role':'assistant','content':reply})
    print("\n",reply,"\n")
