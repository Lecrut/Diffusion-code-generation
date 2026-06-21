def calculate_string_length(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return len(input_string)

class StringLengthAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.length = self._calculate_length()
    
    def _calculate_length(self):
        return len(self.input_string)
    
    def get_length(self):
        return self.length

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "",
        "!!!",
        "   ",
        "123 ABC!@#"
    ]
    for value in sample_values:
        analyzer = StringLengthAnalyzer(value)
        length = analyzer.get_length()
        print(length)