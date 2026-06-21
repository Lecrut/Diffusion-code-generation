class PrimeFinder:
    MAX_RANGE = 100

    @staticmethod
    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        p = 2
        while p * p <= limit:
            if primes[p]:
                for i in range(p * p, limit + 1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, limit) if primes[p]]

    @staticmethod
    def find_primes(start, end):
        if start < 0 or end > PrimeFinder.MAX_RANGE:
            raise ValueError("Range out of bounds")
        return [p for p in PrimeFinder.sieve_of_eratosthenes(end) if p >= start]

if __name__ == '__main__':
    primes = PrimeFinder.find_primes(1, 30)
    print(primes)