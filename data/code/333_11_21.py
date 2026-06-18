class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        return ''.join(word[0] for word in text.split() if word)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World Python Programming"
    result = processor.get_first_chars(sample_input)
    print(result)