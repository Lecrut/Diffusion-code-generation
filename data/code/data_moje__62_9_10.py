import math

def get_divisors(n):
    n = abs(n)
    if n == 0:
        return []
    divisors = set()
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(list(divisors))

if __name__ == '__main__':
    sample_value = 36
    result = get_divisors(sample_value)
    print(result)