class StringProcessor:
    def get_first_chars(self, text):
        return ''.join(word[0] for word in str(text).split())
if __name__ == '__main__':
    processor = StringProcessor()
    input_str = "Hello World Python Programming"
    result = processor.get_first_chars(input_str)
    print(result)