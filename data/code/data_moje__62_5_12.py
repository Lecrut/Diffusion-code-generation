def get_factors(n):
    return list(i for i in range(1, int(n**0.5) + 1) if n % i == 0 for j in (n // i,)) if n > 0 else []

def get_unique_factors(n):
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)

if __name__ == '__main__':
    number = 120
    result = get_unique_factors(number)
    print(result)