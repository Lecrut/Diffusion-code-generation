import math

def find_divisors(n):
    if n <= 0:
        return []
    divisors = set()
    limit = int(math.isqrt(n)) + 1
    for i in range(1, limit):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    n = 999999
    result = find_divisors(n)
    print(result)