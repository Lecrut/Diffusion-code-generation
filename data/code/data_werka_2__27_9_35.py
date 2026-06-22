class ValueChecker:

    def are_different(self, val1, val2):
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    result = checker.are_different(10, 20)
    print(result)
    result = checker.are_different('hello', 'world')
    print(result)
    result = checker.are_different(3.14, 3.14)
    print(result)