import math

def find_factors(n):
    factors = []
    sqrt_n = int(math.isqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

if __name__ == '__main__':
    result = find_factors(7919)
    print(result)