def get_factors(n):
    factors = []
    if n <= 0:
        return factors
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors

def generate_factors(n):
    if n <= 0:
        return
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i

if __name__ == '__main__':
    number = 120
    result = list(generate_factors(number))
    result.sort()
    print(result)