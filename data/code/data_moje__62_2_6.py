def find_factors(n):
    if n < 1:
        return []
    factors = []
    if n == 1:
        factors.append(1)
        return factors
    i = 1
    while i * i < n:
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
        i += 1
    if i * i == n:
        factors.append(i)
    factors.sort()
    return factors

if __name__ == '__main__':
    target_number = 7919
    result = find_factors(target_number)
    print(result)