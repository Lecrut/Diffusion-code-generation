def is_positive(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    return number > 0

class PositiveChecker:
    def __init__(self, values):
        self.values = values

    def check_all(self):
        return {value: is_positive(value) for value in self.values}

if __name__ == '__main__':
    sample_values = [15, -2, 0, 8, -3]
    checker = PositiveChecker(sample_values)
    results = checker.check_all()
    print(results)