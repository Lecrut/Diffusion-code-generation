class GreaterThanTenChecker:
    THRESHOLD = 10

    @staticmethod
    def evaluate(first_value, second_value):
        return first_value > GreaterThanTenChecker.THRESHOLD or second_value > GreaterThanTenChecker.THRESHOLD

if __name__ == '__main__':
    checker = GreaterThanTenChecker()
    val_a = 15
    val_b = 2
    result = checker.evaluate(val_a, val_b)
    print(result)