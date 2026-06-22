def calculate_string_length(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return len(input_string)

class StringLengthAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string

    def analyze_length(self):
        return calculate_string_length(self.input_string)

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello, World!",
        "empty": "",
        "punctuation": "!!!",
        "spaces": "   ",
        "mixed": "123 ABC!@#"
    }

    for key, value in sample_values.items():
        analyzer = StringLengthAnalyzer(value)
        length = analyzer.analyze_length()
        print(f"The length of '{key}' ('{value}') is {length}.")