class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = [word for word in text.split() if word]
        return "".join(word[0].lower() for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World Python Programming"
    result = processor.get_first_chars(sample_input)
    print(result)