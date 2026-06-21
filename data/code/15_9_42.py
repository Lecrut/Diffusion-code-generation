class ValueChecker:

    def are_equal(self, a, b):
        try:
            if a == b:
                return True
            elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return float(a) == float(b)
            elif isinstance(a, str) and isinstance(b, str):
                return a.strip() == b.strip()
            else:
                return False
        except Exception as e:
            raise ValueError(f'Unsupported comparison: {e}')
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, 10.0))
    print(checker.are_equal('hello ', ' hello'))
    print(checker.are_equal([1, 2], [1, 2]))
    print(checker.are_equal(None, None))