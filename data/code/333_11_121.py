class StringProcessor:
    def get_first_chars(self, text):
        result = []
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = text.split()
        for word in words:
            if word and ord(word[0]) >= 97:
                result.append(chr(ord(word[0]) - 32))
            else:
                result.append(word[0].upper())
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "hello world this is a test string"
    output = processor.get_first_chars(sample_input)
    print(output)