import math

def get_divisors(n):
    if n <= 0:
        raise ValueError("Number must be positive")
    divisors = set()
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_values = [12, 28, 100, 1, 97]
    for val in sample_values:
        result = get_divisors(val)
        print(result)