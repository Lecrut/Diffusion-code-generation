import math

def find_divisors(n):
    divisors = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    n = 999999
    result = find_divisors(n)
    print(result)