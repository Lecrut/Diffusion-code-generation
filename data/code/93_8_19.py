class BooleanChecker:
    def __init__(self, val1: bool, val2: bool):
        self.val1 = val1
        self.val2 = val2

    def are_both_false(self) -> bool:
        return not self.val1 and not self.val2

    def get_status(self) -> str:
        if self.val1 and self.val2:
            return "True, True"
        if self.val1:
            return "True, False"
        if self.val2:
            return "False, True"
        return "False, False"

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.are_both_false())
    print(checker.get_status())