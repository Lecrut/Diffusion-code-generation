class EqualityChecker:
    TOLERANCE = 1e-9

    @staticmethod
    def are_identical(a, b):
        if type(a) != type(b):
            return False
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return abs(a - b) < EqualityChecker.TOLERANCE
        return a == b

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.are_identical(10, 10))
    print(checker.are_identical(10.0, 10))
    print(checker.are_identical(10, 10.0))
    print(checker.are_identical("hello", "hello"))
    print(checker.are_identical("hello", "world"))
    print(checker.are_identical(3.14, 3.1400000000000004))
    print(checker.are_identical([1, 2], [1, 2]))