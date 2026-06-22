def find_factors(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    factors = set()
    factors.add(1)
    factors.add(n)
    if n == 2:
        return sorted(factors)
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
        i += 1
    return sorted(factors)

if __name__ == '__main__':
    result = find_factors(7919)
    print(result)