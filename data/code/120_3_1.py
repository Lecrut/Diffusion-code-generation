class ValueChecker:
    def check(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.check(5, 5))
    print(checker.check(10, 5))
    print(checker.check("hello", "hello"))
    print(checker.check(1, 2))