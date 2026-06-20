class BooleanChecker:
    def __init__(self, attr1: bool, attr2: bool):
        self.attr1 = attr1
        self.attr2 = attr2

    def is_false(self, value: bool) -> bool:
        return not value

    def both_false(self) -> bool:
        return self.is_false(self.attr1) and self.is_false(self.attr2)

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.both_false())