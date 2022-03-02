import codecs

from googletrans import Translator
translator = Translator()
with open("history.txt", "w") as f:
            f.write("\n")
print('Введите "помощь" для вывода информации об использовании.')
while True:
    inp = str(input())
    if inp == "выход" or inp == "":
        with open("history.txt", "w") as f:
            f.write("")
        break
    elif inp == "помощь":
        with codecs.open('README.txt', encoding='utf-8') as f:
            print(str(f.read()))
    elif inp == 'история':
        with open("history.txt") as f:
            print(f.read())
        print("\n")
    else:
        result = translator.translate(inp, dest='ru')
        with open("history.txt", "a") as f:
            f.write(f'{result.origin} -> {result.text}' + '\n')
        print(result.text)
