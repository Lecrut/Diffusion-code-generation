def find_factors(n):
    factors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
        i += 1
    return sorted(factors)

if __name__ == '__main__':
    print(find_factors(7919))