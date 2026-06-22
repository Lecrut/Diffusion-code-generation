class BooleanChecker:
    def __init__(self, attr1: bool, attr2: bool):
        self.attr1 = attr1
        self.attr2 = attr2

    def both_are_false(self) -> bool:
        return not self.attr1 and not self.attr2

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.both_are_false())