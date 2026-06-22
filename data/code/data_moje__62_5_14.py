def get_factors(n):
    if n <= 0:
        return
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i

if __name__ == '__main__':
    factors = sorted(get_factors(120))
    print(factors)