class ValueChecker:

    def are_different(self, val1, val2):
        return not self.are_equal(val1, val2)

    def are_equal(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_different(5, 10))
    print(checker.are_different(7, 7))
    print(checker.are_different(3.14, 3.14))
    print(checker.are_different(-1, 1))