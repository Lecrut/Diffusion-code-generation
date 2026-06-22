def calculate_string_length(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return len(input_string)

class StringLengthCalculator:
    def __init__(self, input_string):
        self.input_string = input_string
        if not isinstance(self.input_string, str):
            raise ValueError("Input must be a string")

    def calculate_length(self):
        return len(self.input_string)

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello, World!",
        "empty": "",
        "punctuation": "!!!",
        "spaces": "   ",
        "mixed": "123 ABC!@#"
    }
    
    try:
        result_function = calculate_string_length(sample_values["greeting"])
        print("Function result:", result_function)
        
        calculator = StringLengthCalculator(sample_values["greeting"])
        result_class = calculator.calculate_length()
        print("Class result:", result_class)
    except ValueError as e:
        print(e)