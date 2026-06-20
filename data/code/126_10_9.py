class EqualityChecker:
    @staticmethod
    def check_equality(a, b):
        return a == b

if __name__ == '__main__':
    print(EqualityChecker.check_equality(5, 5))
    print(EqualityChecker.check_equality(10, 5))
    print(EqualityChecker.check_equality("hello", "hello"))
    print(EqualityChecker.check_equality(10.5, 10.5))
    print(EqualityChecker.check_equality(10, 10.0))