class BooleanChecker:
    def __init__(self, first: bool, second: bool):
        self.first = first
        self.second = second

    def are_both_false(self) -> bool:
        return not self.first and not self.second

    def is_first_true(self) -> bool:
        return self.first

    def is_second_true(self) -> bool:
        return self.second

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.are_both_false())
    print(checker.is_first_true())
    print(checker.is_second_true())