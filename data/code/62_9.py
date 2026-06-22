import math

def get_divisors(n):
    if n <= 0:
        return []
    divisors = set()
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_number = 100
    result = get_divisors(sample_number)
    print(result)