class FirstLetterExtractor:
    def extract(self, text):
        words = text.split()
        first_letters = []
        for word in words:
            if word:
                first_letters.append(word[0])
        return first_letters
if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "This is a sample sentence for testing purposes"
    result = extractor.extract(sample_text)
    print(result)