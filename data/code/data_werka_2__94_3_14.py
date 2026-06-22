class BooleanListChecker:
    def __init__(self, values):
        self.values = values

    def has_true(self):
        return any(self.values)

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    checker = BooleanListChecker(sample_data)
    print(checker.has_true())
    sample_data_all_false = [False, False, False]
    checker_all_false = BooleanListChecker(sample_data_all_false)
    print(checker_all_false.has_true())