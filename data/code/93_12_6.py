class BooleanChecker:
    _FALSE_VALUE = False

    def __init__(self, a: bool, b: bool):
        self.a = a
        self.b = b

    def is_false(self, value: bool) -> bool:
        return value is self._FALSE_VALUE

    def check(self) -> bool:
        return self.is_false(self.a) and self.is_false(self.b)

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.check())
    checker = BooleanChecker(True, False)
    print(checker.check())