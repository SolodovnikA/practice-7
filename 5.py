n = int(input())

for i in range(1, int(n ** 0.4)):
  if i ** 3 <= n:
    print(i ** 3, end=' ')
