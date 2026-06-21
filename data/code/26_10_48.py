def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or a float.")

class ThresholdChecker:
    def __init__(self, threshold):
        self.threshold = threshold

    def check_values(self, values):
        results = []
        for value in values:
            validate_input(value)
            if value > self.threshold:
                results.append(True)
            else:
                results.append(False)
        return results

if __name__ == '__main__':
    checker = ThresholdChecker(10)
    values = [2, 13, 8, 17, 5]
    print(checker.check_values(values))