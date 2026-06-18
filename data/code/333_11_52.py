class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        words = [word for word in text.split() if word]
        return ''.join(word[0].upper() for word in words)
if __name__ == '__main__':
    sample_input = "hello world this is a test string"
    processor = StringProcessor()
    result = processor.get_first_chars(sample_input)
    print(result)