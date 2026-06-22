class BooleanChecker:
    def __init__(self, value, values):
        self.value = value
        self.values = values

    def is_any_true(self):
        if self.value:
            return True
        for v in self.values:
            if v:
                return True
        return False

if __name__ == '__main__':
    checker = BooleanChecker(False, [False, True, False])
    print(checker.is_any_true())

    checker2 = BooleanChecker(True, [False, False])
    print(checker2.is_any_true())

    checker3 = BooleanChecker(False, [False, False])
    print(checker3.is_any_true())