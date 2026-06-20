class EqualityChecker:
    def __init__(self):
        self.value1 = 7
        self.value2 = 7

    def check_equal(self):
        return self.value1 == self.value2

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.check_equal())