class ValueChecker:

    def are_equal(self, a, b):
        try:
            if type(a) == type(b):
                return a == b
            elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return float(a) == float(b)
            elif isinstance(a, str) and isinstance(b, list):
                return a == ''.join(b)
            elif isinstance(a, list) and isinstance(b, str):
                return ''.join(a) == b
            else:
                raise ValueError('Unsupported types for comparison')
        except Exception as e:
            print(f'Comparison error: {e}')
            return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(5, 5.0))
    print(checker.are_equal('hello', ['h', 'e', 'l', 'l', 'o']))
    print(checker.are_equal([1, 2, 3], '123'))
    print(checker.are_equal(10, '10'))
    print(checker.are_equal('test', 42))