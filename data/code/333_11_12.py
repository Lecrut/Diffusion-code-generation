class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = [word for word in text.split() if word]
        result = []
        for i, word in enumerate(words):
            if i % 2 == 0 and word[0].isalpha():
                result.append(word[0])
            elif len(result) > 1:
                break
        return "".join(result[:len(words)])
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World Python Programming"
    output = processor.get_first_chars(sample_input)
    print(output)