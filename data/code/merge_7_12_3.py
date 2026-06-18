class ValueChecker:
    @staticmethod
    def compare(a, b):
        return a == b
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.compare(10, 10))
    print(checker.compare(5, 3))
    print(checker.compare("hello", "hello"))
    print(checker.compare(True, True))