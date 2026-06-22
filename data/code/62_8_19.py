import math

def find_divisors(n: int) -> list[int]:
    if n < 1:
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
    result = find_divisors(999999)
    print(result)