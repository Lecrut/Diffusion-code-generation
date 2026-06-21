class ValueChecker:

    def are_equal(self, a, b):
        if type(a) == type(b):
            return a == b
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return float(a) == float(b)
        elif isinstance(a, str) and isinstance(b, str):
            return a.strip() == b.strip()
        else:
            raise ValueError('Unsupported types for comparison')
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, 10.0))
    print(checker.are_equal('hello ', ' hello'))
    print(checker.are_equal([1, 2], [1, 2]))