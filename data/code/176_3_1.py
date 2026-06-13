class StringWordExtractor:
    def extract_unique_words(self, text):
        words = text.lower().split()
        unique_words = set(words)
        return unique_words
if __name__ == '__main__':
    extractor = StringWordExtractor()
    sample_text = "This is a sample sentence for word extraction and testing efficiency"
    result = extractor.extract_unique_words(sample_text)
    print(result)