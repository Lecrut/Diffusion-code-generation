class PrimeChecker:
    def __init__(self):
        self.SMALL_PRIMES = [2, 3]

    def is_small_prime(self, n):
        return n in self.SMALL_PRIMES

    @staticmethod
    def divisible_by_small_primes(n):
        for prime in [2, 3]:
            if n % prime == 0:
                return True
        return False

    def is_prime(self, n):
        if n <= 1:
            return False
        if self.is_small_prime(n):
            return True
        if self.divisible_by_small_primes(n):
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

if __name__ == '__main__':
    checker = PrimeChecker()
    sample_values = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 23, 24, 29, 31, 37]
    for value in sample_values:
        print(f"{value}: {checker.is_prime(value)}")