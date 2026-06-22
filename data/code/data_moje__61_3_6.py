class PrimeChecker:
    PRIMES_UNDER_10 = {2, 3, 5, 7}
    SPLIT_POINT = 10

    @staticmethod
    def _check_small(n):
        return n in PrimeChecker.PRIMES_UNDER_10

    @staticmethod
    def _check_large(n):
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = int(n**0.5)
        i = 5
        while i <= limit:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @classmethod
    def is_prime(cls, n):
        if n < 2:
            return False
        if n < cls.SPLIT_POINT:
            return cls._check_small(n)
        return cls._check_large(n)

if __name__ == '__main__':
    print(PrimeChecker.is_prime(29))
    print(PrimeChecker.is_prime(30))
    print(PrimeChecker.is_prime(4))
    print(PrimeChecker.is_prime(0))