print('Справка:')
print(' Для выбора варианта ответа предлагается ввести 1, если вы хотите выбрать 1 вариант и 2, если 2')
print(' Для возвращения на предыдущий уровень введите Назад')
print()
c = open('texts\count.txt')
count = str(c.readline())
print('Выберите квест вводом числа от 1 до ' + count)
namefile = str(input())
intpr = bool(True)
ints = str('0123456789')
for i in range(0,len(namefile)) :
    if (ints.find(namefile[i]) == -1) :
        intpr = False
        break
if (len(namefile) == 0) :
    intpr = False
while not(intpr) :
    print('Ввод неверен')
    print('Выберите квест вводом числа от 1 до ' + count)
    namefile = str(input())
    intpr = True
    for i in range(0,len(namefile)) :
        if (ints.find(namefile[i]) == -1) :
            intpr = False
            break
    if (len(namefile) == 0) :
        intpr = False
    if (intpr) :
        if (int(namefile) >= 1 and int(namefile) <= int(count)) :
            break
        else :
            intpr = False
f = open('texts\\' + namefile + 'text.txt')
t = bool(True)
scenario = {}
text = f.readlines()
i = int(0)
while (i < len(text)) :
    num = text[i].strip()
    num = '\n'.join(num.split('\\n'))
    i += 1
    ask = text[i].strip()
    ask = '\n'.join(ask.split('\\n'))
    i += 1
    first = text[i].strip()
    first = '\n'.join(first.split('\\n'))
    i += 1
    second = text[i].strip()
    second = '\n'.join(second.split('\\n'))
    i += 1
    num = '\n'.join(num.split('\\n'))
    scenario[num] = [str(ask), str(first), str(second)]
#Ввод закончен
asknum = str('0')
while (scenario[asknum][0].find('конец игры') == -1) :
    print()
    print(scenario[asknum][0])
    print('Что делать?')
    print(scenario[asknum][1])
    print(scenario[asknum][2])
    answer = str(input())
    while not(answer == '1' or answer == '2' or answer == 'Назад') :
        print('Для выбора варианта ответа предлагается ввести 1, если вы хотите выбрать первый вариант и 2, если второй')
        answer = str(input())
    if (answer == '1') :
        asknum = asknum + '0'
    else :
        if (answer == '2') :
            asknum = asknum + '1'
        else :
            if (answer == 'Назад') :
                if (len(asknum)>1) :
                    print('Возвращение на предыдущий уровень')
                    asknum = asknum[0:len(asknum)-1]
print(scenario[asknum][0])
print('Если хотите покинуть игру, введите любой символ')
a = input()
