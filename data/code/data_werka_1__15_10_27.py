class ValueChecker:

    def are_equal(self, a, b):
        try:
            return a == b
        except TypeError:
            try:
                if isinstance(a, (int, float)) and isinstance(b, str):
                    return a == float(b)
                elif isinstance(a, str) and isinstance(b, (int, float)):
                    return float(a) == b
                else:
                    return False
            except ValueError:
                return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, '10'))
    print(checker.are_equal('20.5', 20.5))
    print(checker.are_equal('hello', 'world'))
    print(checker.are_equal([1, 2], [1, 2]))
    print(checker.are_equal((1, 2), (1, 3)))