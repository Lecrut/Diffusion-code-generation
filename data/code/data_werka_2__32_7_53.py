class StringLengthCalculator:
    DEFAULT_SAMPLE = "Hello, World!"
    
    @staticmethod
    def calculate_length(input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return len(input_string)

if __name__ == '__main__':
    sample_values = [
        StringLengthCalculator.DEFAULT_SAMPLE,
        "",
        "!!!",
        "   ",
        "123 ABC!@#"
    ]
    
    for value in sample_values:
        length = StringLengthCalculator.calculate_length(value)
        print(f"The length of '{value}' is {length}.")