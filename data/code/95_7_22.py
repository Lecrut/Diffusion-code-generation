class ConditionChecker:
    POSITIVE_THRESHOLD = 0
    EVEN_MODULUS = 2

    @staticmethod
    def is_positive(value):
        return value > ConditionChecker.POSITIVE_THRESHOLD

    @staticmethod
    def is_even(value):
        return value % ConditionChecker.EVEN_MODULUS == 0

    def check(self, first, second, third):
        if not self.is_positive(first):
            return False
        if not self.is_even(second):
            return False
        product = first * second
        if product == 0:
            return False
        return third % product == 0

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check(3, 2, 6)
    print(result)