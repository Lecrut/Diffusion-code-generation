class FirstLetterExtractor:
    DELIMITER = ' '

    def extract(self, text):
        words = text.split(self.DELIMITER)
        first_letters = [word[0] for word in words if word]
        return ''.join(first_letters)

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "Implementing a unique solution"
    result = extractor.extract(sample_text)
    print(result)