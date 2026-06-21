class PrimeChecker:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def is_divisible(n, divisor):
        return n % divisor == 0

    def check_prime(self):
        if self.number <= 1:
            return False
        if self.number <= 3:
            return True
        if PrimeChecker.is_divisible(self.number, 2) or PrimeChecker.is_divisible(self.number, 3):
            return False
        i = 5
        while i * i <= self.number:
            if PrimeChecker.is_divisible(self.number, i) or PrimeChecker.is_divisible(self.number, i + 2):
                return False
            i += 6
        return True

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 10, 11, 13, 17, 19, 23, 29, 31]
    for value in sample_values:
        checker = PrimeChecker(value)
        print(f"{value}: {checker.check_prime()}")