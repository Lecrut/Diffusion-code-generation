class StringProcessor:
    def get_first_chars(self, text):
        words = [word for word in text.split() if word]
        return ''.join(word[0].lower() for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    input_str = "Hello World Python Programming"
    result = processor.get_first_chars(input_str)
    print(result)