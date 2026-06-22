class ThresholdChecker:
    def __init__(self, threshold):
        self.threshold = threshold

    def is_greater_than_threshold(self, value):
        return isinstance(value, float) and value > self.threshold

if __name__ == '__main__':
    sample_value1 = 5.0
    sample_value2 = 2.5
    threshold_value = 3.0

    checker = ThresholdChecker(threshold_value)
    
    result1 = checker.is_greater_than_threshold(sample_value1)
    result2 = checker.is_greater_than_threshold(sample_value2)

    print(result1)
    print(result2)