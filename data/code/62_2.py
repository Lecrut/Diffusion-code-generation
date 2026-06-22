def find_factors(n):
    factors = []
    if n <= 1:
        return [1] if n == 1 else []
    factors.append(1)
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors

if __name__ == '__main__':
    result = find_factors(7919)
    print(result)