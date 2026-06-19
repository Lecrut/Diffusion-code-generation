class ValueChecker:

    def are_different(self, val1, val2):
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_different(10, 20))
    print(checker.are_different('hello', 'hello'))
    print(checker.are_different([1, 2], [1, 2]))
    print(checker.are_different({'a': 1}, {'a': 1}))