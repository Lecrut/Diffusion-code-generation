import math

def generate_primes_up_to(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    primes = generate_primes_up_to(limit)
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [2, 3, 4, 5, 16, 17, 18, 19, 20, 97, 100, 101, 7919, 7921]
    for val in test_values:
        print(f"{val}: {is_prime(val)}")