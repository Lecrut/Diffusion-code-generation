class ValueChecker:

    def are_different(self, val1, val2):
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_different(42, 43))
    print(checker.are_different('hello', 'hello'))