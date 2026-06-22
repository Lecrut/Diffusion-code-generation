def find_factors(n):
    factors = []
    if n < 1:
        return factors
    factors.append(1)
    if n == 1:
        return factors
    limit = int(n ** 0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            factors.append(i)
            other = n // i
            if other != i:
                factors.append(other)
    factors.append(n)
    factors.sort()
    return factors

if __name__ == '__main__':
    number = 7919
    result = find_factors(number)
    print(result)