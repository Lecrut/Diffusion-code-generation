class ValueChecker:
    def are_unequal(self, a: int, b: int) -> bool:
        return a != b
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"Are 10 and 5 unequal? {checker.are_unequal(10, 5)}")
    print(f"Are 7 and 7 unequal? {checker.are_unequal(7, 7)}")
    print(f"Are -1 and 1 unequal? {checker.are_unequal(-1, 1)}")
    print(f"Are 0 and 0 unequal? {checker.are_unequal(0, 0)}")