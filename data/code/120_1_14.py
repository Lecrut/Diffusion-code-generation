class EqualityChecker:
    def compare(self, value1, value2):
        return value1 == value2

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.compare(42, 42))
    print(checker.compare('hello', 'world'))
    print(checker.compare([1, 2], [1, 2]))
    print(checker.compare({'a': 1}, {'a': 1}))