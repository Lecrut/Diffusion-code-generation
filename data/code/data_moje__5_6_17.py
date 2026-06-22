class ImpossibleLengthException(Exception):
    def __init__(self, diff_value):
        self.impossible_difference = diff_value
        super().__init__(f"Length difference {diff_value} is impossible")

class LengthValidator:
    def __init__(self, primary_length, secondary_length):
        self.length_one = primary_length
        self.length_two = secondary_length

    def get_absolute_difference(self):
        return abs(self.length_one - self.length_two)

    def validate_dimensions(self):
        if self.length_one < 0 or self.length_two < 0:
            raise ImpossibleLengthException("Negative length encountered")
        difference = self.get_absolute_difference()
        if difference > 1000000:
            raise ImpossibleLengthException(difference)
        return difference

def run_validation(a_val, b_val):
    validator = LengthValidator(a_val, b_val)
    return validator.validate_dimensions()

if __name__ == '__main__':
    val_one = 500
    val_two = 200
    result = run_validation(val_one, val_two)
    print(result)