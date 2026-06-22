def get_factors(n):
    if n <= 0:
        return []
    factors = []
    step = 1 if n % 2 != 0 else 1
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
        i += 1
    factors.sort()
    return factors

if __name__ == '__main__':
    target_number = 120
    result = get_factors(target_number)
    print(result)