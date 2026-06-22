import math

def get_divisors(n: int) -> list[int]:
    if n <= 0:
        return []
    divisors = []
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample = 28
    result = get_divisors(sample)
    print(result)