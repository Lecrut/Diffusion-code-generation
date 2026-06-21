def calculate_string_length(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return len(input_string)

class StringLengthCalculator:
    def __init__(self, input_string):
        self.length = calculate_string_length(input_string)
    
    def get_length(self):
        return self.length

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "",
        "!!!",
        "   ",
        "123 ABC!@#"
    ]
    for s in sample_strings:
        calculator = StringLengthCalculator(s)
        print(calculator.get_length())