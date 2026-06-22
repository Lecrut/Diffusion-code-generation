def generate_primes_up_to(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
        i += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def is_prime_by_prime_check(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n ** 0.5)
    primes = generate_primes_up_to(limit)
    for prime in primes:
        if prime < 2:
            continue
        if n % prime == 0:
            return False
    return True

if __name__ == '__main__':
    test_values = [2, 3, 4, 17, 20, 23, 100, 101, 997, 1000]
    for value in test_values:
        print(value, is_prime_by_prime_check(value))