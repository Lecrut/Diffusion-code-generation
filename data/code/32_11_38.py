class StringAnalyzer:
    @staticmethod
    def calculate_character_count(input_string):
        return len(input_string)

if __name__ == '__main__':
    sample_input = "Qwen, Alibaba Cloud's AI Assistant"
    character_count = StringAnalyzer.calculate_character_count(sample_input)
    print(character_count)