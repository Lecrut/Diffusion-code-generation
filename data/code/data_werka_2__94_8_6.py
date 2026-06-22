class BooleanChecker:
    def __init__(self, values):
        self.values = values

    def has_true(self):
        if not self.values:
            return False
        for val in self.values:
            if val:
                return True
        return False

    def count_true(self):
        return sum(1 for val in self.values if val)

    def all_false(self):
        return not self.has_true()

if __name__ == '__main__':
    sample_values = [False, False, True, False]
    checker = BooleanChecker(sample_values)
    print(checker.has_true())
    print(checker.count_true())
    print(checker.all_false())