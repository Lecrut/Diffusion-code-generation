class FirstLetterExtractor:
    def extract(self, text):
        if not text:
            return ""
        words = text.split()
        result = []
        for word in words:
            for char in word:
                if char.isalpha():
                    result.append(char)
                    break
        return "".join(result)

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "Hello, world! This is a test."
    print(extractor.extract(sample_text))
    another_text = " 123 numbers and ! symbols"
    print(extractor.extract(another_text))
    empty_text = ""
    print(extractor.extract(empty_text))