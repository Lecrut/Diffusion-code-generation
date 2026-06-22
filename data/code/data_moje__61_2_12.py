class PrimeChecker:
    def __init__(self, value):
        self.value = value

    def is_prime(self):
        n = self.value
        if n < 2:
            return False
        if n in (2, 3):
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
    samples = [10, 11, 13, 17, 20, 25, 29, 31, 37, 40]
    results = []
    for n in samples:
        checker = PrimeChecker(n)
        results.append(f"{n}: {checker.is_prime()}")
    print(results)