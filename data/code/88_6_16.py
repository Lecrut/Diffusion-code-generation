class FlagChecker:
    def __init__(self, flag1: int, flag2: int):
        self.flag1 = flag1
        self.flag2 = flag2

    def are_both_true(self) -> bool:
        return (self.flag1 & 1 == 1) and (self.flag2 & 1 == 1)

if __name__ == '__main__':
    checker1 = FlagChecker(1, 1)
    print(f"are_both_true(1, 1): {checker1.are_both_true()}")

    checker2 = FlagChecker(0, 1)
    print(f"are_both_true(0, 1): {checker2.are_both_true()}")

    checker3 = FlagChecker(1, 0)
    print(f"are_both_true(1, 0): {checker3.are_both_true()}")

    checker4 = FlagChecker(0, 0)
    print(f"are_both_true(0, 0): {checker4.are_both_true()}")