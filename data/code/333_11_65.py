class StringProcessor:
    def first_char_per_word(self, s: str) -> str:
        return ''.join(word[0] for word in s.split())
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello World Python Programming"
    result = processor.first_char_per_word(test_input)
    print(result)