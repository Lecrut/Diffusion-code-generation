class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string

    def calculate_character_count(self):
        return len(self.input_string)

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    analyzer = StringAnalyzer(sample_input)
    character_count = analyzer.calculate_character_count()
    print(character_count)

    another_sample_input = "Hello, World!"
    another_analyzer = StringAnalyzer(another_sample_input)
    another_character_count = another_analyzer.calculate_character_count()
    print(another_character_count)