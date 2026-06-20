class BoolChecker:

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def both_false(self):
        return not self.attr1 and (not self.attr2)
if __name__ == '__main__':
    checker = BoolChecker(False, False)
    print(checker.both_false())