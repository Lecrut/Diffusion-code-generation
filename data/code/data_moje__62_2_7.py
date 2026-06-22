def find_factors(n):
    if n < 1:
        return []
    factors = set()
    limit = int(n ** 0.5) + 1
    for i in range(1, limit):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(list(factors))

if __name__ == '__main__':
    number = 7919
    result = find_factors(number)
    print(result)