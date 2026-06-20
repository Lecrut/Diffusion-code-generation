class FlagChecker:

    def __init__(self, flag1: int, flag2: int):
        self.flag1 = flag1
        self.flag2 = flag2

    def are_both_true(self) -> bool:
        return self.flag1 & 1 == 1 and self.flag2 & 1 == 1
if __name__ == '__main__':
    checker1 = FlagChecker(3, 5)
    print(checker1.are_both_true())
    checker2 = FlagChecker(4, 6)
    print(checker2.are_both_true())