class ValueChecker:

    def are_equal(self, a, b):
        if type(a) == type(b):
            return a == b
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return float(a) == float(b)
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return float(a) == float(b)
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return float(a) == float(b)
        else:
            return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, 10.0))
    print(checker.are_equal('10', 10))
    print(checker.are_equal('10.5', 10.5))
    print(checker.are_equal('abc', 'def'))
    print(checker.are_equal([1, 2], [1, 2]))