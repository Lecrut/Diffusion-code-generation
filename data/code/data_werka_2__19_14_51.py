class PrimeChecker:
    def __init__(self):
        self.small_primes = [2, 3]

    def is_prime(self, n):
        if n <= 1:
            return False
        if n in self.small_primes:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

if __name__ == '__main__':
    checker = PrimeChecker()
    sample_values = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 23, 24, 29]
    for value in sample_values:
        print(f"{value}: {checker.is_prime(value)}")