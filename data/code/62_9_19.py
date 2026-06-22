import math

def get_divisors(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    divisors = set()
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_values = [12, 28, 49, 100, 97]
    for value in sample_values:
        result = get_divisors(value)
        print(f"Divisors of {value}: {result}")