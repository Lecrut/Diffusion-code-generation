class InequalityChecker:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def check_inequality(self):
        if not isinstance(self.value1, (int, float)) or not isinstance(self.value2, (int, float)):
            raise ValueError("Both values must be numeric (int or float).")
        return self.value1 != self.value2

if __name__ == '__main__':
    value1 = 42
    value2 = 3.14
    checker = InequalityChecker(value1, value2)
    result = checker.check_inequality()
    print(result)