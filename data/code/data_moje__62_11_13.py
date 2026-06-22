import math

def get_divisors(n):
    if n <= 0:
        return []
    divisors = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(list(divisors))

if __name__ == '__main__':
    print(get_divisors(28))
    print(get_divisors(100))