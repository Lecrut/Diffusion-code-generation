def find_factors(n):
    factors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
        i += 1
    return sorted(factors)

if __name__ == '__main__':
    result = find_factors(7919)
    print(result)