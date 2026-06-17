class StringProcessor:
    def first_char_of_each_word(self, text: str) -> str:
        return ''.join(word[0] for word in text.split() if word)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello world this is a test string"
    result = processor.first_char_of_each_word(sample_input)
    print(result)