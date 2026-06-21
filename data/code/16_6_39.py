def is_positive(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float")
    return value > 0

class PositiveChecker:
    def __init__(self, values):
        self.values = values

    def check_all(self):
        results = {}
        for val in self.values:
            try:
                results[val] = is_positive(val)
            except ValueError as e:
                results[val] = str(e)
        return results

if __name__ == '__main__':
    sample_values = [3.14, -2.71, 0.0, 1e-10, -1e-10, "not a number", None]
    checker = PositiveChecker(sample_values)
    print(checker.check_all())