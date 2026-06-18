class StringProcessor:
    def get_first_chars(self, text):
        words = [word for word in text.split() if len(word) > 0]
        return ''.join([word[0].upper() for word in words])
if __name__ == '__main__':
    processor = StringProcessor()
    input_str = "hello world this is a test string"
    output_str = processor.get_first_chars(input_str)
    print(output_str)