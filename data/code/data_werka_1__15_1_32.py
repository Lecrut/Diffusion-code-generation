class ValueChecker:

    def are_equal(self, a: object, b: object) -> bool:
        return a == b
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, 10))
    print(checker.are_equal('hello', 'world'))
    print(checker.are_equal([1, 2, 3], [1, 2, 3]))
    print(checker.are_equal({'key': 'value'}, {'key': 'value'}))