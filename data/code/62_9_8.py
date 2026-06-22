import math

def get_divisors(n):
    if n == 0:
        return []
    if n < 0:
        n = abs(n)
    divisors = set()
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_values = [28, 100, 49, 1]
    for num in sample_values:
        result = get_divisors(num)
        print(result)