import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    print(get_divisors(28))
    print(get_divisors(100))
    print(get_divisors(13))