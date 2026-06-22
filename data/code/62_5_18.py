def get_factors(n):
    if n <= 0:
        return iter([])
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return iter(factors)

if __name__ == '__main__':
    result = list(get_factors(120))
    print(result)