import math
def get_prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                count += 1
                n //= d
            factors.append((d, count))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return factors
def compute_target_index(n):
    prime_factors = get_prime_factors(n)
    sorted_factors = sorted(prime_factors, key=lambda x: -x[1])
    target_exponent = 0
    for p, count in sorted_factors:
        if count > target_exponent:
            target_exponent = count
    return sorted_factors[0][1]
if __name__ == '__main__':
    sample_values = [60, 24576, 98304]
    for val in sample_values:
        print(f"Input: {val}, Target Index (Max Exponent): {compute_target_index(val)}")