class ValueChecker:

    def check_for_zero(self, value: float) -> bool:
        return value == 0.0
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.check_for_zero(0))
    print(checker.check_for_zero(-0.0))
    print(checker.check_for_zero(123.456))
    print(checker.check_for_zero(0.0001))