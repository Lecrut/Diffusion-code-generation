import math

def collect_primes_below(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    sieve_size = n
    sieve = [True] * sieve_size
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.isqrt(n - 1)) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    result = []
    for index, is_prime_flag in enumerate(sieve):
        if is_prime_flag:
            result.append(index)
    return result

def is_prime_via_primes(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    if limit < 2:
        return True
    primes_to_check = collect_primes_below(limit + 1)
    for p in primes_to_check:
        if n % p == 0:
            return False
    return True

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 10, 13, 15, 97, 100, 7919, 8000]
    for val in sample_values:
        result = is_prime_via_primes(val)
        print(result)