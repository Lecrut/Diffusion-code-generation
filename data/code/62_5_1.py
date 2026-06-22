def find_factors(n):
    return (i for i in range(1, int(n**0.5) + 1) if n % i == 0)

def get_all_factors(n):
    factors = set()
    for i in find_factors(n):
        factors.add(i)
        factors.add(n // i)
    return sorted(factors)

if __name__ == '__main__':
    number = 120
    result = get_all_factors(number)
    print(result)