def get_factors(n):
    return (i for i in range(1, int(n**0.5) + 1) if n % i == 0)

def get_all_factors(n):
    factors = list(get_factors(n))
    result = []
    for f in factors:
        result.append(f)
        if f != n // f:
            result.append(n // f)
    result.sort()
    return result

if __name__ == '__main__':
    number = 120
    print(get_all_factors(number))