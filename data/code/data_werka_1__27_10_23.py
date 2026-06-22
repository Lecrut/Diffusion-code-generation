class ValueChecker:
    def are_different(self, val1, val2):
        return val1 != val2

if __name__ == '__main__':
    checker = ValueChecker()
    result = checker.are_different(42, '42')
    print(result)