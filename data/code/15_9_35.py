class ValueChecker:

    def are_equal(self, a, b):
        try:
            return a == b
        except TypeError:
            if isinstance(a, (int, float)) and isinstance(b, str):
                try:
                    num_b = float(b)
                    return a == num_b
                except ValueError:
                    return False
            elif isinstance(a, str) and isinstance(b, (int, float)):
                try:
                    num_a = float(a)
                    return num_a == b
                except ValueError:
                    return False
            else:
                return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, '10'))
    print(checker.are_equal('20.5', 20.5))
    print(checker.are_equal('abc', 123))
    print(checker.are_equal([1, 2], [1, 2]))
    print(checker.are_equal((1, 2), (1, 2)))