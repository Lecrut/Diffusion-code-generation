class BooleanListChecker:
    def __init__(self, booleans):
        self.booleans = booleans

    def has_true(self):
        return any(self.booleans)

if __name__ == '__main__':
    checker = BooleanListChecker([False, False, True, False])
    print(checker.has_true())