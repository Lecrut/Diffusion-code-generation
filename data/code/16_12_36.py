class PositiveChecker:
    def __init__(self, values):
        self.values = values

    def is_positive(self, number):
        return number > 0

    def check_all(self):
        return {value: self.is_positive(value) for value in self.values}

if __name__ == '__main__':
    sample_values = [-5, 0, 3.14, -2.718, 10]
    checker = PositiveChecker(sample_values)
    print(checker.check_all())