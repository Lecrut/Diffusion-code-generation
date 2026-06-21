class EqualityChecker:
    @staticmethod
    def are_strictly_equal(a, b):
        if a is None or b is None:
            return a == b
        else:
            return a is b and a == b

if __name__ == '__main__':
    print(EqualityChecker.are_strictly_equal(None, None))
    print(EqualityChecker.are_strictly_equal(10, 10))
    print(EqualityChecker.are_strictly_equal('hello', 'hello'))
    print(EqualityChecker.are_strictly_equal([], []))
    print(EqualityChecker.are_strictly_equal({}, {}))
    print(EqualityChecker.are_strictly_equal(None, 0))