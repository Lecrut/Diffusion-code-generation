class BooleanChecker:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def are_both_false(self):
        return not self.val1 and not self.val2

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.are_both_false())
    checker2 = BooleanChecker(True, False)
    print(checker2.are_both_false())
    checker3 = BooleanChecker(False, True)
    print(checker3.are_both_false())
    checker4 = BooleanChecker(True, True)
    print(checker4.are_both_false())