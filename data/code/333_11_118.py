class StringProcessor:
    def get_first_chars(self, text):
        words = text.split()
        return ''.join(word[0] for word in words) if words else ''
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World Python Programming"
    result = processor.get_first_chars(sample_input)
    print(result)