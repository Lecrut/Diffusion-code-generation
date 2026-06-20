class EqualityChecker:
    def __init__(self):
        self.value1 = 20
        self.value2 = 20

    def check_values(self):
        return self.value1 == self.value2

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.check_values())