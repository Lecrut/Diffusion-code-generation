class BooleanListChecker:
    def __init__(self, lst):
        self.lst = lst

    def has_true(self):
        return any(self.lst)

if __name__ == '__main__':
    checker = BooleanListChecker([False, False, True, False])
    print(checker.has_true())