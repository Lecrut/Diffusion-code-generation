def get_factors(n):
    return (i for i in range(1, int(n**0.5) + 1) if n % i == 0)

if __name__ == '__main__':
    n = 120
    factors = sorted(set(
        i for i in get_factors(n)
    ) | set(
        n // i for i in get_factors(n)
    ))
    print(factors)