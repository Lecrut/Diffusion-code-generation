class WordExtractor:
    @staticmethod
    def extract_first_word(input_string):
        words = input_string.split()
        return words[0] if words else ""

if __name__ == '__main__':
    sample_input = "This is a sample string to test the function"
    result = WordExtractor.extract_first_word(sample_input)
    print(result)