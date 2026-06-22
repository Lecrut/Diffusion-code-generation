class BooleanChecker:
    def __init__(self, left: bool, right: bool):
        self.left = left
        self.right = right

    def check_both_false(self) -> bool:
        return self.left is False and self.right is False

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.check_both_false())
    checker2 = BooleanChecker(True, False)
    print(checker2.check_both_false())