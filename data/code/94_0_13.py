class BooleanChecker:
    def __init__(self, values):
        if not isinstance(values, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        for val in values:
            if not isinstance(val, bool):
                raise ValueError("All elements must be boolean values")
        self.values = list(values)

    def has_true(self):
        return any(self.values)

if __name__ == '__main__':
    data = [False, False, True, False]
    checker = BooleanChecker(data)
    result = checker.has_true()
    print(result)