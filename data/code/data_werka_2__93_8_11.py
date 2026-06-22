class BooleanChecker:
    def __init__(self, val_a: bool, val_b: bool):
        self.val_a = val_a
        self.val_b = val_b

    def both_false(self) -> bool:
        return not self.val_a and not self.val_b

    def check(self) -> bool:
        return self.both_false()

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.check())
    print(checker.both_false())