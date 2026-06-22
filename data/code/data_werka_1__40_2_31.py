class FirstLetterExtractor:
    def __init__(self):
        self.separator = ' '

    def extract(self, text):
        words = text.split(self.separator)
        first_letters = [word[0] for word in words if word]
        return ''.join(first_letters)

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "Object-oriented programming is a paradigm"
    result = extractor.extract(sample_text)
    print(result)