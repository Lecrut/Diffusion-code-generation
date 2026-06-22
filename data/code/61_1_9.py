def get_primes_up_to(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
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
    limit = int(n**0.5) + 1
    primes = get_primes_up_to(limit)
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True

if __name__ == '__main__':
    sample_values = [2, 3, 4, 5, 16, 17, 25, 29, 97, 100]
    for val in sample_values:
        result = is_prime(val)
        print(f"{val}: {result}")