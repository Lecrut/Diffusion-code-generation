class BooleanChecker:
    def __init__(self, values):
        self.values = values

    def has_true(self):
        return any(self.values)

    def count_true(self):
        return sum(self.values)

if __name__ == '__main__':
    checker = BooleanChecker([False, False, True, False])
    print(checker.has_true())
    print(checker.count_true())