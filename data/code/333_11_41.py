class StringProcessor:
    def get_first_chars(self, text):
        result = []
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = text.split()
        for word in words:
            if word and (word[0].isalpha()):
                result.append(word[0])
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_input = "Hello world! This is a Python script."
    output = processor.get_first_chars(test_input)
    print(output)