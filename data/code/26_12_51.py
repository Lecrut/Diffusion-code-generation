class ThresholdChecker:
    VALUE_TYPES = (int, float)
    THRESHOLD_TYPES = (int, float)

    @staticmethod
    def validate_value(value):
        if not isinstance(value, ThresholdChecker.VALUE_TYPES):
            raise TypeError('Value must be an integer or float')

    @staticmethod
    def validate_threshold(threshold):
        if not isinstance(threshold, ThresholdChecker.THRESHOLD_TYPES):
            raise TypeError('Threshold must be an integer or float')

    def exceeds_threshold(self, value, threshold):
        self.validate_value(value)
        self.validate_threshold(threshold)
        return value > threshold

if __name__ == '__main__':
    sample_values = [
        (10, 5),
        (3.5, 4.0),
        (-2, -3),
        ('a', 1),
        (7, 'b')
    ]
    checker = ThresholdChecker()
    for value, threshold in sample_values:
        try:
            result = checker.exceeds_threshold(value, threshold)
            print(f'Value: {value}, Threshold: {threshold} -> Exceeds: {result}')
        except Exception as e:
            print(f'Error with Value: {value}, Threshold: {threshold} -> {e}')