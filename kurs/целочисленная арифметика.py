#шаг6 урок 2.5
b = int(input())
q = int(input())
n = int(input())
nn = (n - 1)
print( b * (q ** nn))

#шаг7 урок 2.5
n=int(input())
print(n // 100)

#шаг8 урок 2.5
h=int(input())
m=int(input())
print(m//h)
print(m%h)

#шаг9 урок 2.5
n=int(input())
print(n//2+n%2)

#шаг10 урок 2.5
n=int(input())
print((n-1) // 4+1)

#шаг11 урок 2.5
t=int(input())
print(t, f'мин - это {t//60} час {t % 60} минут.')

#шаг13 урок 2.5
eha = int(input())
print('Сумма цифр =', yeha//100 + (yeha % 100) // 10 + yeha%10)
print('Произведение цифр =', (yeha//100) * ((yeha % 100) // 10) * (yeha%10))

#шаг14 урок 2.5
abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
print(a, b, c, sep='')
print(a,c,b, sep='')
print(b,a,c, sep='')
print(b,c,a, sep='')
print(c,a,b, sep='')
print(c,b,a, sep='')

#шаг15 урок 2.5
m = int(input())
m1 = m // 1000
m2 = (m // 100) % 10
m3 = (m // 10) % 10
m4 = m % 10
print("Цифра в позиции тысяч равна", m1)
print("Цифра в позиции сотен равна", m2)
print("Цифра в позиции десятков равна", m3)
print("Цифра в позиции единиц равна", m4)
