class Validator:
    POSITIVE_THRESHOLD = 0
    EVEN_MODULUS = 2
    MAX_MAGNITUDE = 100

    def __init__(self):
        self.status_messages = []

    def _validate_single(self, value):
        if value <= self.POSITIVE_THRESHOLD:
            raise ValueError(f"Input {value} must be positive")
        if value % self.EVEN_MODULUS != 0:
            raise ValueError(f"Input {value} must be even")
        if value >= self.MAX_MAGNITUDE:
            raise ValueError(f"Input {value} must be less than 100")
        return True

    def combine_and_report(self, a, b, c):
        self.status_messages = []
        inputs = [a, b, c]
        valid_inputs = []
        
        for val in inputs:
            try:
                self._validate_single(val)
                valid_inputs.append(val)
                self.status_messages.append(f"{val} passed all checks")
            except ValueError as e:
                self.status_messages.append(str(e))
        
        combined_sum = sum(valid_inputs)
        
        return {
            "original_inputs": [a, b, c],
            "valid_inputs": valid_inputs,
            "sum_of_valid": combined_sum,
            "report": self.status_messages
        }

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 20, 30)
    print(result)