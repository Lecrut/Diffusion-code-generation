class EqualityChecker:
    @staticmethod
    def check_identity(a, b):
        return a is b

    @staticmethod
    def check_value_equality(a, b):
        return a == b

    @classmethod
    def are_strictly_equal(cls, a, b):
        if a is None or b is None:
            return cls.check_identity(a, b)
        else:
            return cls.check_identity(a, b) and cls.check_value_equality(a, b)

if __name__ == '__main__':
    print(EqualityChecker.are_strictly_equal(None, None))
    print(EqualityChecker.are_strictly_equal(10, 10))
    print(EqualityChecker.are_strictly_equal('hello', 'hello'))
    print(EqualityChecker.are_strictly_equal([], []))
    print(EqualityChecker.are_strictly_equal({}, {}))
    print(EqualityChecker.are_strictly_equal(None, 0))