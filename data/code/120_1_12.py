class EqualityChecker:
    @staticmethod
    def are_values_equal(value1, value2):
        return value1 == value2

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.are_values_equal(42, 42))
    print(checker.are_values_equal('hello', 'world'))
    print(checker.are_values_equal([1, 2], [1, 2]))
    print(checker.are_values_equal({'a': 1}, {'a': 1}))