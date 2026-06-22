class ValueChecker:

    def are_equal(self, a, b):
        try:
            return a == b
        except TypeError:
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return float(a) == float(b)
            elif isinstance(a, str) and isinstance(b, (int, float)):
                return float(a) == float(b)
            elif isinstance(a, (int, float)) and isinstance(b, str):
                return float(a) == float(b)
            else:
                raise ValueError('Unsupported types for comparison')
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, 10.0))
    print(checker.are_equal('20', 20))
    print(checker.are_equal(30, '30'))
    print(checker.are_equal('40', '50'))
    try:
        print(checker.are_equal([1, 2], (1, 2)))
    except ValueError as e:
        print(e)