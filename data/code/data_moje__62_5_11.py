def find_factors(n):
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i

if __name__ == '__main__':
    number = 120
    factors = list(sorted(find_factors(number)))
    print(factors)