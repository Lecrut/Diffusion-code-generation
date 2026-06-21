class ConditionChecker:
    def __init__(self):
        self.threshold = 10
        self.multiplier = 2
        self.modulus = 5

    def check_all(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number")

        is_positive = value > 0
        is_below_threshold = value < self.threshold
        is_even_multiple = (value * self.multiplier) % self.modulus == 0

        return is_positive and is_below_threshold and is_even_multiple

if __name__ == '__main__':
    checker = ConditionChecker()
    sample_value = 4
    result = checker.check_all(sample_value)
    print(result)
    sample_value2 = 15
    result2 = checker.check_all(sample_value2)
    print(result2)
    sample_value3 = -2
    result3 = checker.check_all(sample_value3)
    print(result3)