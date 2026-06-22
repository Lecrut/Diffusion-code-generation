class ValueChecker:

    def are_equal(self, a, b):
        try:
            if a == b:
                return True
            elif str(a) == str(b):
                return True
            else:
                return False
        except Exception as e:
            raise ValueError(f'Comparison failed: {e}')
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, '10'))
    print(checker.are_equal(3.14, 3.14))
    print(checker.are_equal('hello', 'world'))
    print(checker.are_equal([1, 2], [1, 2]))
    print(checker.are_equal({'a': 1}, {'a': 1}))