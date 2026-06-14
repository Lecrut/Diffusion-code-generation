import math
def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes
if __name__ == '__main__':
    limit = 50
    prime_numbers = sieve_of_eratosthenes(limit)
    print(prime_numbers)