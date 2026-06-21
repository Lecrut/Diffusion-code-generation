def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def calculate_string_length(input_string):
    validate_input(input_string)
    return len(input_string)

class StringLengthCalculator:
    def __init__(self, input_string):
        self.input_string = input_string
        validate_input(self.input_string)
    
    def get_length(self):
        return len(self.input_string)

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "",
        "!!!",
        "   ",
        "123 ABC!@#"
    ]
    for value in sample_values:
        length_function_result = calculate_string_length(value)
        print(f"The length of '{value}' using function is {length_function_result}.")
        
        calculator = StringLengthCalculator(value)
        length_method_result = calculator.get_length()
        print(f"The length of '{value}' using class method is {length_method_result}.")