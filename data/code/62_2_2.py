def find_factors(n):
    factors = []
    if n <= 0:
        return factors
    if n == 1:
        return [1]
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if i * i != n:
                factors.append(n // i)
        i += 1
    factors.sort()
    return factors

if __name__ == '__main__':
    result = find_factors(7919)
    print(result)