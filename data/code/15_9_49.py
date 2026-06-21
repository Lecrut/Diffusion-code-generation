class ValueChecker:

    def are_equal(self, a, b):
        try:
            if type(a) == type(b):
                return a == b
            elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return float(a) == float(b)
            elif isinstance(a, str) and isinstance(b, list):
                return a == ''.join(map(str, b))
            elif isinstance(a, list) and isinstance(b, str):
                return ''.join(map(str, a)) == b
            else:
                raise ValueError('Unsupported types for comparison')
        except Exception as e:
            print(f'Comparison error: {e}')
            return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, '10'))
    print(checker.are_equal(3.14, 3.14))
    print(checker.are_equal('hello', ['h', 'e', 'l', 'l', 'o']))
    print(checker.are_equal([1, 2], (1, 2)))
    print(checker.are_equal({'a': 1}, {'a': 1}))