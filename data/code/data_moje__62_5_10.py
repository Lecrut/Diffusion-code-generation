def get_factors(n):
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return sorted(result)

if __name__ == '__main__':
    number = 120
    factors = list(get_factors(number))
    print(factors)