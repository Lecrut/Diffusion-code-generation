class BooleanChecker:
    def __init__(self, values):
        self.values = values

    def check_any_true(self):
        return any(self.values)

if __name__ == '__main__':
    checker = BooleanChecker([False, False, True, False])
    result = checker.check_any_true()
    print(result)