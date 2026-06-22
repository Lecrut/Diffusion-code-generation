import math

def find_divisors(n):
    if n <= 0:
        return []
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)

if __name__ == '__main__':
    print(find_divisors(28))
    print(find_divisors(100))
    print(find_divisors(1))