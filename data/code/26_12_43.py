class ThresholdChecker:
    SUPPORTED_TYPES = (int, float)

    @staticmethod
    def is_valid_number(value):
        return isinstance(value, ThresholdChecker.SUPPORTED_TYPES)

    def exceeds_threshold(self, value, threshold):
        if not ThresholdChecker.is_valid_number(value):
            raise TypeError('Value must be an integer or float')
        if not ThresholdChecker.is_valid_number(threshold):
            raise TypeError('Threshold must be an integer or float')
        return value > threshold

if __name__ == '__main__':
    sample_values = [
        (10, 5),
        (3.5, 4.0),
        (-2, -3),
        ('a', 1),
        (7, 'b'),
        (8, 8)
    ]
    checker = ThresholdChecker()
    for value, threshold in sample_values:
        try:
            result = checker.exceeds_threshold(value, threshold)
            print(f'Value: {value}, Threshold: {threshold} -> Exceeds: {result}')
        except Exception as e:
            print(f'Error with Value: {value}, Threshold: {threshold} -> {e}')