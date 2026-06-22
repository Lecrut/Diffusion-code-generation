def find_factors(n):
    if n <= 0:
        return []
    factors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
        i += 1
    return sorted(list(factors))
if __name__ == '__main__':
    number = 7919
    result = find_factors(number)
    print(result)