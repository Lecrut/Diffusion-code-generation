class BooleanChecker:
    def __init__(self, data):
        self.data = data

    def has_true(self):
        return any(self.data)

    def all_false(self):
        return not any(self.data)

if __name__ == '__main__':
    checker = BooleanChecker([False, False, False])
    print(checker.has_true())
    print(checker.all_false())