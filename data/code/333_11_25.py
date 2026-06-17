class StringProcessor:
    def first_chars(self, s: str) -> str:
        words = s.split()
        return ''.join(word[0] for word in words if word)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello World Python Programming"
    result = processor.first_chars(test_input)
    print(result)