import math
def prime_factorization(n):
    factors = {}
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        d += 1
    if n > 1:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1
    return factors
def compute_target_index(n):
    factors = prime_factorization(n)
    sorted_primes = sorted(factors.keys())
    target_prime = max(sorted_primes, key=lambda p: (factors[p], -p)) if len(sorted_primes) > 0 else None
    return factors.get(target_prime, 1)
if __name__ == '__main__':
    sample_values = [630, 840, 924]
    for val in sample_values:
        index_result = compute_target_index(val)
        print(f"Input: {val}, Target Index Result: {index_result}")