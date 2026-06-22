class BooleanChecker:
    _EMPTY_RESULT = False

    def __init__(self, values):
        self.values = values

    @staticmethod
    def has_true(values):
        if not values:
            return BooleanChecker._EMPTY_RESULT
        return any(values)

    def check(self):
        return self.has_true(self.values)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    checker = BooleanChecker(sample_list)
    result = checker.check()
    print(result)