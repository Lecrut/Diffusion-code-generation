class ValueChecker:

    def check_for_zero(self, value: int) -> bool:
        return value == 0
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.check_for_zero(0))
    print(checker.check_for_zero(1))
    print(checker.check_for_zero(-1))