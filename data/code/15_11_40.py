class EqualityChecker:

    def __init__(self):
        self.identity_check = lambda x, y: x is y
        self.value_check = lambda x, y: x == y

    def are_strictly_equal(self, a, b):
        if a is None or b is None:
            return self.identity_check(a, b)
        else:
            return self.identity_check(a, b) and self.value_check(a, b)
if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.are_strictly_equal(None, None))
    print(checker.are_strictly_equal(10, 10))
    print(checker.are_strictly_equal('hello', 'hello'))
    print(checker.are_strictly_equal([], []))
    print(checker.are_strictly_equal({}, {}))
    print(checker.are_strictly_equal(None, 0))