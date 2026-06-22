class ValueChecker:
    def are_different(self, val1, val2):
        return val1 != val2

if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_different(42, 24))
    print(checker.are_different("hello", "world"))
    print(checker.are_different([1, 2, 3], [1, 2, 3]))