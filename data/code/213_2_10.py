class PrimeNumberFinder:
    MAX_RANGE = 100

    @staticmethod
    def sieve_of_eratosthenes(n):
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n) if is_prime[p]]

    def find_primes(self):
        return self.sieve_of_eratosthenes(self.MAX_RANGE)

if __name__ == '__main__':
    finder = PrimeNumberFinder()
    print(finder.find_primes())