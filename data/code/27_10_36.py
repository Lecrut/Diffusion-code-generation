class ValueChecker:

    def are_different(self, val1, val2):
        return self._compare(val1, val2)

    @staticmethod
    def _compare(a, b):
        return a != b
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_different(10, 20))
    print(checker.are_different(5.5, 5.5))
    print(checker.are_different('hello', 'world'))
    print(checker.are_different(True, 1))