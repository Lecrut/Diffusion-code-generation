class InvalidLengthError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        self.message = message

class LengthValidator:
    def __init__(self, len_one, len_two):
        self.len_one = len_one
        self.len_two = len_two

    def validate_and_compute_difference(self):
        if self.len_one < 0:
            raise InvalidLengthError(f"First length {self.len_one} is invalid.")
        if self.len_two < 0:
            raise InvalidLengthError(f"Second length {self.len_two} is invalid.")
        
        diff = abs(self.len_one - self.len_two)
        
        if self.len_one == 0 and self.len_two > 100:
            raise InvalidLengthError("Impossible difference detected: zero vs large value.")
        if self.len_two == 0 and self.len_one > 100:
            raise InvalidLengthError("Impossible difference detected: zero vs large value.")
            
        return diff

def execute_test_scenario(a_val, b_val):
    validator = LengthValidator(a_val, b_val)
    return validator.validate_and_compute_difference()

if __name__ == '__main__':
    sample_a = 42
    sample_b = 15
    result = execute_test_scenario(sample_a, sample_b)
    print(result)
    
    try:
        execute_test_scenario(-5, 10)
    except InvalidLengthError as e:
        print(e.message)
    
    try:
        execute_test_scenario(0, 500)
    except InvalidLengthError as e:
        print(e.message)