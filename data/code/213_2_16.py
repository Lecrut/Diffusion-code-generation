def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit) if is_prime[p]]
    return prime_numbers

if __name__ == '__main__':
    sample_limit = 50
    primes = sieve_of_eratosthenes(sample_limit)
    print(primes)