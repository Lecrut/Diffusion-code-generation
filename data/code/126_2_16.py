class EqualityChecker:
    def compare(self, value1, value2):
        return value1 == value2

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.compare(10, 10))
    print(checker.compare(5.5, 5.5))
    print(checker.compare("hello", "hello"))
    print(checker.compare(1, 2))
    print(checker.compare(True, True))
    print(checker.compare(10, 10.0))