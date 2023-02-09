lit = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
w = open('output.txt', 'w')

with open('input.txt', 'r') as f:
    numbers = f.read()

numbers = numbers.split()
for i in numbers:
    x = -1 
    y = -1
    num = ''
    for j in '0123456789':
        if (i.find(j) != len(i)-1-(i[::-1].find(j))) and i.find(j) != -1:
            x = i.find(j)
            y = len(i) - 1 - i[::-1].find(j)
            num = lit['0123456789'.find(j)]
    if x!=-1:
        w.write(i[:x] + num + i[y+1:] + ' ')
    else:
        w.write(i+' ')
    
w.close()