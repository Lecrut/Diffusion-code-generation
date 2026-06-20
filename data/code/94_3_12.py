class BooleanChecker:
    def __init__(self, booleans):
        self.booleans = booleans

    def has_true(self):
        return any(self.booleans)

if __name__ == '__main__':
    checker = BooleanChecker([False, False, True, False])
    print(checker.has_true())