def calculate_character_count(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return len(input_string)

class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_character_count(self):
        return calculate_character_count(self.input_string)

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    analyzer = StringAnalyzer(sample_input)
    character_count = analyzer.get_character_count()
    print(character_count)