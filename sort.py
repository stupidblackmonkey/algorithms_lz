import random
N = input('введите колво чисел для сортировки пузырьком')
a = []
N = int(N)
q = 0
for i in range(N):
    a.append(random.randint(1, 1000000))
print('список = ' , a)  # вывод исходного неотсортированного списка

# Сама сортировка методом "пузырька"
for i in range(N-1):
    for j in range(N-1-i):
        if a[j+1] > a[j]:
            a[j+1], a[j] = a[j], a[j+1]  
            q += 1
            print (a)
print ('отсортированный список : = ' , a)
print ('колво сравнений в алгоритме сортировки пузырьком' , q)



N1 = input('введите колво чисел для сортировки выбором')
a1 = []
N1 = int(N1)
d = 0
for i in range(N1):
    a1.append(random.randint(1, 1000000))
print('список = ' , a1)  # вывод исходного неотсортированного списка
k = 0
while k < N - 1:
    m = k
    w = k + 1
    while w < N:
        if a1[w] > a1[m]:
            m = w
        w += 1
    a1[k], a1[m] = a1[m], a1[i]
    k += 1
    d += 1
    print(a1)
print('отсортированный список : = ' , a1)
print('колво сравнений в алгоритме сортировке выбором' , d)