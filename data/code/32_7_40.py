def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def calculate_string_length(input_string):
    validate_input(input_string)
    return len(input_string)

class StringLengthAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        validate_input(self.input_string)
    
    def get_total_character_count(self):
        return len(self.input_string)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "",
        "!!!",
        "   ",
        "123 ABC!@#"
    ]
    
    for sample in sample_strings:
        length_function_result = calculate_string_length(sample)
        print(f"Length calculated by function: {length_function_result}")
        
        analyzer = StringLengthAnalyzer(sample)
        length_method_result = analyzer.get_total_character_count()
        print(f"Length calculated by class method: {length_method_result}")