class InvalidLengthError(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.invalid_value = value
        self.message = message

class LengthAnalyzer:
    def __init__(self, length_one, length_two):
        self.length_one = length_one
        self.length_two = length_two

    def _validate_single(self, name, value):
        if value < 0:
            raise InvalidLengthError(f"{name} cannot be negative", value)

    def validate(self):
        self._validate_single("First length", self.length_one)
        self._validate_single("Second length", self.length_two)
        return True

    def calculate_difference(self):
        self.validate()
        diff = abs(self.length_one - self.length_two)
        return diff

    def analyze(self):
        self.validate()
        return self.length_one + self.length_two, self.length_one * self.length_two

if __name__ == '__main__':
    sample_one = LengthAnalyzer(12.5, 8.0)
    diff_result = sample_one.calculate_difference()
    print(diff_result)
    sum_prod = sample_one.analyze()
    print(sum_prod)
    sample_two = LengthAnalyzer(-3.0, 5.0)
    try:
        sample_two.validate()
    except InvalidLengthError as err:
        print(f"Caught error: {err.message} for value {err.invalid_value}")