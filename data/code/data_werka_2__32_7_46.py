def calculate_string_length(input_string):
    return len(input_string)

class StringLengthAnalyzer:
    def __init__(self, input_data):
        self.input_data = input_data
    def analyze(self):
        if isinstance(self.input_data, dict):
            results = {}
            for key, value in self.input_data.items():
                if not isinstance(value, str):
                    raise ValueError("All values must be strings")
                results[key] = calculate_string_length(value)
            return results
        elif isinstance(self.input_data, list):
            results = []
            for item in self.input_data:
                if not isinstance(item, str):
                    raise ValueError("All items must be strings")
                results.append(calculate_string_length(item))
            return results
        else:
            raise ValueError("Input data must be a dictionary or list of strings")

if __name__ == '__main__':
    sample_values = {
        "greeting": "Hello, World!",
        "empty": "",
        "punctuation": "!!!",
        "spaces": "   ",
        "mixed": "123 ABC!@#"
    }
    analyzer = StringLengthAnalyzer(sample_values)
    result = analyzer.analyze()
    for key, length in result.items():
        print(f"The length of '{key}' is {length}.")