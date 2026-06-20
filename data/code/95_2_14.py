class TripleChecker:
    @staticmethod
    def is_positive(num):
        return num > 0

    @staticmethod
    def is_even(num):
        return num % 2 == 0

    @staticmethod
    def sum_divisible_by_third(a, b, c):
        return (a + b) % c == 0

    def validate(self, a, b, c):
        if all([self.is_positive(num) for num in [a, b, c]]) and \
           self.is_even(a) and self.is_even(b) and \
           self.sum_divisible_by_third(a, b, c):
            return True
        return False

if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(2, 4, 6))
    print(checker.validate(1, 2, 3))
    print(checker.validate(2, 2, 5))
    print(checker.validate(3, 4, 6))