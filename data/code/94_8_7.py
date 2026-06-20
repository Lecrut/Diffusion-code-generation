class TruthChecker:
    def __init__(self, values):
        self.values = values

    def check_at_least_one_true(self):
        return any(self.values)

if __name__ == '__main__':
    checker1 = TruthChecker([True, False, True, False])
    print(checker1.check_at_least_one_true())

    checker2 = TruthChecker(['', 0, None, 'hello'])
    print(checker2.check_at_least_one_true())

    checker3 = TruthChecker([])
    print(checker3.check_at_least_one_true())