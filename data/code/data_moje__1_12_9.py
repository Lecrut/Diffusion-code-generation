class WeightValidator:
    def __init__(self, raw_measurements):
        self.raw_measurements = raw_measurements

    def extract_positive_weights(self):
        valid_weights = []
        for measurement in self.raw_measurements:
            try:
                numeric_value = float(measurement)
                if numeric_value > 0:
                    valid_weights.append(numeric_value)
            except (ValueError, TypeError):
                continue
        return valid_weights

if __name__ == '__main__':
    test_data = ['42.5', '0', '-10', 'NaN', '3.14', 'abc', '100', '  ', '-0.5', '25']
    validator = WeightValidator(test_data)
    print(validator.extract_positive_weights())