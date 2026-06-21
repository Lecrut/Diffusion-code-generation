class ValueChecker:

    def are_equal(self, a, b):
        try:
            if a == b:
                return True
            elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return float(a) == float(b)
            elif isinstance(a, str) and isinstance(b, (str, int, float)):
                return str(a) == str(b)
            elif isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
                return len(a) == len(b) and all((self.are_equal(x, y) for x, y in zip(a, b)))
            else:
                raise ValueError('Unsupported types for comparison')
        except Exception as e:
            print(f'Comparison error: {e}')
            return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(1, 1.0))
    print(checker.are_equal('1', 1))
    print(checker.are_equal([1, 2], (1, 2)))
    print(checker.are_equal([1, 2], [1, '2']))
    print(checker.are_equal('hello', 'world'))