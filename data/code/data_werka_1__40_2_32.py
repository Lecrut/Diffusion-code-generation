class FirstLetterExtractor:
    def extract(self, text):
        words = text.split()
        if not words:
            return ""
        first_letters = [word[0] for word in words if word]
        return ''.join(first_letters)

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "Extract the first letter of each word"
    result = extractor.extract(sample_text)
    print(result)