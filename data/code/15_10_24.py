class ValueChecker:

    def are_equal(self, a, b):
        try:
            if type(a) == type(b):
                return a == b
            elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return float(a) == float(b)
            elif isinstance(a, str) and isinstance(b, (int, float)):
                return float(a) == float(b)
            elif isinstance(b, str) and isinstance(a, (int, float)):
                return float(b) == float(a)
            else:
                return False
        except Exception as e:
            return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(5, 5.0))
    print(checker.are_equal('10', 10))
    print(checker.are_equal('abc', 'abc'))
    print(checker.are_equal('abc', 123))
    print(checker.are_equal([1, 2], [1, 2]))