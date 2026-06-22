def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")
    return value

def check_threshold_or(val_a, val_b):
    a = validate_integer(val_a)
    b = validate_integer(val_b)
    threshold = 10
    condition_a = a > threshold
    condition_b = b > threshold
    return condition_a or condition_b

class ThresholdChecker:
    def __init__(self, value_one, value_two):
        self.val_one = validate_integer(value_one)
        self.val_two = validate_integer(value_two)
        self.threshold = 10

    def evaluate(self):
        return self.val_one > self.threshold or self.val_two > self.threshold

if __name__ == '__main__':
    checker = ThresholdChecker(12, 8)
    result = checker.evaluate()
    print(result)