class EqualityChecker:
    def are_values_equal(self, a, b):
        return a == b

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.are_values_equal(10, 10))
    print(checker.are_values_equal(10, 20))
    print(checker.are_values_equal('hello', 'hello'))
    print(checker.are_values_equal('hello', 'world'))