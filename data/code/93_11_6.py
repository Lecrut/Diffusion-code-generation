class BooleanChecker:
    EXPECTED_FALSE = False

    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        return a is BooleanChecker.EXPECTED_FALSE and b is BooleanChecker.EXPECTED_FALSE

if __name__ == '__main__':
    print(BooleanChecker.evaluate(False, False))
    print(BooleanChecker.evaluate(True, False))
    print(BooleanChecker.evaluate(False, True))
    print(BooleanChecker.evaluate(True, True))