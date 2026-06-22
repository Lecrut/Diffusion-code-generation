class BooleanChecker:
    def __init__(self, first: bool, second: bool):
        self.first = first
        self.second = second

    def are_both_false(self) -> bool:
        return not self.first and not self.second

    def get_status(self) -> str:
        if self.are_both_false():
            return "both_false"
        return "not_both_false"

if __name__ == '__main__':
    checker = BooleanChecker(False, False)
    print(checker.are_both_false())
    print(checker.get_status())