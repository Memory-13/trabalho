
N = int(input('digite um número:'))

def func(N):
    return sum([x for x in range(N -1, 0, -1) if x % 3 == 0 or x % 5 == 0])

print(func(N))