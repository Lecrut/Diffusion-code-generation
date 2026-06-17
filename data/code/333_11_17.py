class StringProcessor:
    def get_first_chars(self, s: str) -> str:
        if not s.strip():
            return ""
        words = [word for word in s.split()]
        result = []
        for i, word in enumerate(words):
            first_char = word[0].lower()
            result.append(first_char)
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello world Python Programming"
    output = processor.get_first_chars(test_input)
    print(output)