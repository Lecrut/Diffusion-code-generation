def get_factors(n):
    factors = []
    if n < 1:
        return factors
    if n == 1:
        return [1]
    limit = int(n ** 0.5)
    for i in range(1, limit + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors

if __name__ == '__main__':
    number = 7919
    result = get_factors(number)
    print(result)