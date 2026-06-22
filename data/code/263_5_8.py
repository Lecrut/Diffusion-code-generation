class PrimeChecker:
    PRIME_CHECK_LIMIT = 2

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        if n <= PrimeChecker.PRIME_CHECK_LIMIT:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    print(PrimeChecker.is_prime(29))
    print(PrimeChecker.is_prime(15))