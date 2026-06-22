class BooleanChecker:
    def __init__(self, values):
        self.values = values

    def has_true(self):
        return any(self.values)

    def has_false(self):
        return any(not v for v in self.values)

    def count_true(self):
        return sum(1 for v in self.values if v)

if __name__ == '__main__':
    checker = BooleanChecker([False, True, False])
    print(checker.has_true())
    print(checker.has_false())
    print(checker.count_true())