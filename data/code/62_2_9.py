def find_factors(n):
    factor_pairs = {}
    boundary = int(n ** 0.5)
    for candidate in range(1, boundary + 1):
        if n % candidate == 0:
            factor_pairs[candidate] = n // candidate
    unique_factors = sorted(set(factor_pairs.keys()) | set(factor_pairs.values()))
    return unique_factors

if __name__ == '__main__':
    prime_target = 7919
    computed_factors = find_factors(prime_target)
    print(computed_factors)