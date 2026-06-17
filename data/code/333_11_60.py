class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        if not text.strip():
            return ""
        words = [word for word in text.split()]
        result = ''.join(word[0].lower() for word in words)
        return result
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World Python Programming"
    output = processor.get_first_chars(sample_input)
    print(output)