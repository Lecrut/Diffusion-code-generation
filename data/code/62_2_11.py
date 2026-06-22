def find_factors(n):
    if n <= 0:
        return []
    factors = []
    if n == 1:
        return [1]
    factors.append(1)
    if n > 1:
        factors.append(n)
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            factors.append(i)
            quotient = n // i
            if quotient != i:
                factors.append(quotient)
    factors.sort()
    return factors

if __name__ == '__main__':
    number = 7919
    result = find_factors(number)
    print(result)