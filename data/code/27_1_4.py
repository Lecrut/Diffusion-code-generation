class ValueChecker:
    def are_unequal(self, a: int, b: int) -> bool:
        return a != b
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"10 and 5 are unequal: {checker.are_unequal(10, 5)}")
    print(f"7 and 7 are unequal: {checker.are_unequal(7, 7)}")
    print(f"-1 and 1 are unequal: {checker.are_unequal(-1, 1)}")
    print(f"0 and 0 are unequal: {checker.are_unequal(0, 0)}")
    print(f"3.14 and 3.15 are unequal: {checker.are_unequal(3.14, 3.15)}")