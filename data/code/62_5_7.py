def get_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

def generate_factors(n):
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i

if __name__ == '__main__':
    number = 120
    factors_list = get_factors(number)
    print(factors_list)
    factors_gen = sorted(generate_factors(number))
    print(factors_gen)