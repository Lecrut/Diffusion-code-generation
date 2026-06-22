class PrimeChecker:
    MIN_PRIME = 2

    @staticmethod
    def is_prime(n):
        if n <= PrimeChecker.MIN_PRIME - 1:
            return False
        if n % 2 == 0:
            return n == PrimeChecker.MIN_PRIME
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    print(PrimeChecker.is_prime(29))
    print(PrimeChecker.is_prime(15))