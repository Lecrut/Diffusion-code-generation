class EqualityChecker:
    @staticmethod
    def check(val1, val2):
        return val1 == val2

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.check(5, 5))
    print(checker.check(10, 5))
    print(checker.check("hello", "hello"))
    print(checker.check(3.14, 3.1400000000000004))