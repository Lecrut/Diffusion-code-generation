class StringProcessor:
    def get_first_chars(self, text):
        result = []
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = text.split()
        for word in words:
            if word and len(word) > 0:
                result.append(word[0])
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello world Python programming is fun"
    output = processor.get_first_chars(test_input)
    print(output)