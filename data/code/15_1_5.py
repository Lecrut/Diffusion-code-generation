class ValueChecker:
    def are_equal(self, a: int, b: int) -> bool:
        return a == b
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"are_equal(10, 10): {checker.are_equal(10, 10)}")
    print(f"are_equal(5, 3): {checker.are_equal(5, 3)}")
    print(f"are_equal('a', 'a'): {checker.are_equal('a', 'a')}")
    print(f"are_equal(True, True): {checker.are_equal(True, True)}")
    print(f"are_equal(1.5, 1.5): {checker.are_equal(1.5, 1.5)}")