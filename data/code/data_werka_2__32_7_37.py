class StringLengthCalculator:
    def __init__(self, input_string):
        self.input_string = input_string

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
    
    calculator = StringLengthCalculator(sample_values["greeting"])
    result = calculator.calculate_length()
    print(result)