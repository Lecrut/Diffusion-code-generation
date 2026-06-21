def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]

if __name__ == '__main__':
    start = 10
    end = 50
    prime_numbers = sieve_of_eratosthenes(end)
    print(prime_numbers[start:end+1])