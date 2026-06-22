def find_factors(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    factors = []
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
    number = 7919
    result = find_factors(number)
    print(result)