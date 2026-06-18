class StringProcessor:
    def get_first_chars(self, s):
        return ''.join(word[0] for word in s.split())
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello World Python Programming"
    result = processor.get_first_chars(test_input)
    print(result)