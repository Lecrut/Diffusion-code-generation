class BooleanChecker:
    def __init__(self, attr1: bool, attr2: bool):
        self.attr1 = attr1
        self.attr2 = attr2

    @staticmethod
    def check_both_false(attr1: bool, attr2: bool) -> bool:
        return not attr1 and not attr2

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.check_both_false())