class StringAnalyzer:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def calculate_character_count(self):
        return len(self.input_string)

if __name__ == '__main__':
    sample_input1 = "Hello, World!"
    analyzer1 = StringAnalyzer(sample_input1)
    character_count1 = analyzer1.calculate_character_count()
    print(character_count1)

    sample_input2 = "Alibaba Cloud"
    analyzer2 = StringAnalyzer(sample_input2)
    character_count2 = analyzer2.calculate_character_count()
    print(character_count2)