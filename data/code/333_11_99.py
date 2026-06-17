class StringProcessor:
    def get_first_chars(self, s):
        words = [word for word in s.split() if word]
        return ''.join(word[0].upper() for word in words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "hello world this is a sample string"
    result = processor.get_first_chars(test_input)
    print(result)