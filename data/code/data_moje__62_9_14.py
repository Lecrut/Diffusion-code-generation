import math

def get_divisors(n):
    if n < 1:
        return []
    divisors = set()
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    number = 100
    result = get_divisors(number)
    print(result)