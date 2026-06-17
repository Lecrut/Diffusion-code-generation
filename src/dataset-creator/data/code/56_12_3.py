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
    final_prime = None
    for p, count in prime_factors:
        if count == target_exponent and final_prime is None:
            final_prime = p
    if final_prime is not None:
        pass
    return final_prime
if __name__ == '__main__':
    sample_values = [12, 60, 75]
    for val in sample_values:
        result = compute_target_index(val)
        print(f"Input: {val} -> Target Index/Value: {result}")