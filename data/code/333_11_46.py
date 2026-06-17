class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = [word for word in text.split() if word]
        result = []
        for word in words:
            char_code = ord(word[0])
            result.append(chr(char_code))
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello World Python Programming"
    output = processor.get_first_chars(test_input)
    print(output)