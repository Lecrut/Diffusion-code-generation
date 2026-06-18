class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        return ''.join(word[0] for word in text.split() if word)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello world this is a sample string"
    result = processor.get_first_chars(test_input)
    print(result)