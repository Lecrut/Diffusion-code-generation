class BooleanChecker:

    def __init__(self, attr1: bool, attr2: bool):
        self.attr1 = attr1
        self.attr2 = attr2

    def both_false(self) -> bool:
        return not self.attr1 and (not self.attr2)
if __name__ == '__main__':
    checker1 = BooleanChecker(False, False)
    print(checker1.both_false())
    checker2 = BooleanChecker(True, False)
    print(checker2.both_false())
    checker3 = BooleanChecker(False, True)
    print(checker3.both_false())
    checker4 = BooleanChecker(True, True)
    print(checker4.both_false())