class BooleanChecker:
    def __init__(self, val_a: bool, val_b: bool):
        self.val_a = val_a
        self.val_b = val_b

    def are_both_false(self) -> bool:
        return self.val_a is False and self.val_b is False

    def get_status(self) -> str:
        if self.val_a and self.val_b:
            return "both true"
        if self.val_a:
            return "a true"
        if self.val_b:
            return "b true"
        return "both false"

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.are_both_false())
    print(checker.get_status())