class FirstLetterExtractor:
    def extract(self, text):
        return ''.join(word[0] for word in text.split() if word)

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "Unique implementation with early returns"
    result = extractor.extract(sample_text)
    print(result)