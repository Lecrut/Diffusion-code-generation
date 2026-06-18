class StringProcessor:
    def first_chars(self, text: str) -> str:
        words = [word for word in text.split() if word]
        return ''.join(word[0].lower() for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World Python Programming"
    result = processor.first_chars(sample_input)
    print(result)