class IntegerValidator:
    def __init__(self, values):
        self.values = values
        self._validate_inputs()

    def _validate_inputs(self):
        for val in self.values:
            if not isinstance(val, int):
                raise ValueError(f"Expected integer, got {type(val).__name__}")

    def _check_positive(self, n):
        return n > 0

    def _check_even(self, n):
        return n % 2 == 0

    def _check_less_than_100(self, n):
        return n < 100

    def process(self):
        results = []
        for val in self.values:
            results.append({
                'value': val,
                'is_positive': self._check_positive(val),
                'is_even': self._check_even(val),
                'is_less_than_100': self._check_less_than_100(val)
            })
        return results

if __name__ == '__main__':
    sample_values = [42, -3, 100]
    validator = IntegerValidator(sample_values)
    output = validator.process()
    print(output)