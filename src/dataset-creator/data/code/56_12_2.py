import math
from functools import reduce
from operator import mul
def get_prime_factors(n):
    factors = []
    d = 2
    temp_n = n
    while d * d <= temp_n:
        if temp_n % d == 0:
            count = 0
            while temp_n % d == 0:
                count += 1
                temp_n //= d
            factors.append((d, count))
        d += 1
    if temp_n > 1:
        factors.append((temp_n, 1))
    return factors
def compute_target_index(n):
    prime_factors = get_prime_factors(n)
    total_exponents = sum(count for _, count in prime_factors)
    target_idx = (total_exponents // 2) + 1
    if n == 0 or n < 4:
        return -1
    return target_idx
if __name__ == '__main__':
    sample_values = [6, 30, 84]
    for val in sample_values:
        result_index = compute_target_index(val)
        print(f"Input: {val}, Target Index: {result_index}")