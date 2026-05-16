class ValueChecker:
    def are_unequal(self, a: int, b: int) -> bool:
        return a != b
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_unequal(10, 20))
    print(checker.are_unequal(5, 5))
    print(checker.are_unequal(-1, 1))
    print(checker.are_unequal(0, -1))