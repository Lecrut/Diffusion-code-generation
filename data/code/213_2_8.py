def sieve_of_eratosthenes(limit):
    if limit < 2:
        raise ValueError("Limit must be greater than or equal to 2")
    
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    
    return [p for p in range(2, limit + 1) if primes[p]]

if __name__ == '__main__':
    result = sieve_of_eratosthenes(30)
    print(result)