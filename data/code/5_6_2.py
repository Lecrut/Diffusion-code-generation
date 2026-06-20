class ImpossibleLengthError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.error_message = message

class DimensionPair:
    def __init__(self, value_one, value_two):
        self.value_one = value_one
        self.value_two = value_two

    def check_validity(self):
        if self.value_one < 0:
            raise ImpossibleLengthError(f"First dimension {self.value_one} is negative")
        if self.value_two < 0:
            raise ImpossibleLengthError(f"Second dimension {self.value_two} is negative")
        return True

    def compute_ratio(self):
        if self.value_one == 0 and self.value_two == 0:
            return 1.0
        if self.value_two == 0:
            return float('inf')
        return self.value_one / self.value_two

    def analyze_difference(self):
        self.check_validity()
        abs_diff = abs(self.value_one - self.value_two)
        ratio = self.compute_ratio()
        if abs_diff > 5000 or ratio > 1000000 or (ratio < 1e-6 and self.value_one > 0):
            raise ImpossibleLengthError(f"Dimensions {self.value_one} and {self.value_two} differ impossibly")
        return {"diff": abs_diff, "ratio": ratio}

def main_execution():
    pair_instance = DimensionPair(450, 455)
    result = pair_instance.analyze_difference()
    print(result)
    try:
        bad_pair = DimensionPair(10, -5)
        bad_pair.analyze_difference()
    except ImpossibleLengthError as e:
        print(e.error_message)

if __name__ == '__main__':
    main_execution()