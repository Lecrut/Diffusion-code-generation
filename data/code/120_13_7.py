class ValueChecker:
    def check_equality(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.check_equality(5, 5))
    print(checker.check_equality(10, 5))
    print(checker.check_equality("hello", "hello"))
    print(checker.check_equality(3.14, 3.1400000000000004))