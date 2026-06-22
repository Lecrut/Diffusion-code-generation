class PrimeChecker:
    SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]

    @staticmethod
    def is_small_prime(n):
        return n in PrimeChecker.SMALL_PRIMES

    @staticmethod
    def check_divisibility(n, start, step):
        i = start
        while i * i <= n:
            if n % i == 0:
                return False
            i += step
        return True

    @classmethod
    def is_prime(cls, n):
        if n <= 1:
            return False
        if cls.is_small_prime(n):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        return cls.check_divisibility(n, 5, 6) and cls.check_divisibility(n, 7, 4)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 23, 24, 29]
    for value in sample_values:
        print(f"{value}: {PrimeChecker.is_prime(value)}")