class BoolChecker:

    def __init__(self, a: bool, b: bool):
        self.a = a
        self.b = b

    def both_false(self) -> bool:
        return not self.a and (not self.b)
if __name__ == '__main__':
    checker = BoolChecker(False, False)
    print(checker.both_false())