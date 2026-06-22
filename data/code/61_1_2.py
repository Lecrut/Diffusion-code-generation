import math

def generate_primes_up_to(limit):
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    primes = generate_primes_up_to(limit)
    for prime in primes:
        if n % prime == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5, 10, 13, 17, 20, 97, 100]
    for val in test_values:
        print(f"{val}: {is_prime(val)}")