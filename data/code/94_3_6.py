class BooleanChecker:
    def __init__(self, values):
        self.values = values

    def has_true(self):
        return any(self.values)

    def count_true(self):
        return sum(1 for v in self.values if v)

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    checker = BooleanChecker(sample_data)
    print(checker.has_true())
    print(checker.count_true())