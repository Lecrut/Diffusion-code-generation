class FirstLetterExtractor:
    def extract(self, text):
        words = text.split()
        return ''.join(word[0] for word in words)

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "This is a sample text"
    print(extractor.extract(sample_text))