def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for p in range(2, limit):
        if is_prime[p]:
            primes.append(p)
    return primes

class PrimeFinder:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.primes = sieve_of_eratosthenes(self.end)

    def find_primes_in_range(self):
        return [p for p in self.primes if p >= self.start and p <= self.end]

if __name__ == '__main__':
    prime_finder = PrimeFinder(1, 30)
    print(prime_finder.find_primes_in_range())