class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def extract_even_index_chars(self):
        return ''.join(char for index, char in enumerate(self.input_string) if index % 2 == 0)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    processor = StringProcessor(sample_phrase)
    result = processor.extract_even_index_chars()
    print(result)