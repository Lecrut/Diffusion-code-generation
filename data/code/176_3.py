class StringWordExtractor:
    def extract_words(self, text):
        words = set()
        for word in text.lower().split():
            words.add(word)
        return words
if __name__ == '__main__':
    extractor = StringWordExtractor()
    sample_text = "This is a sample sentence for word extraction and testing."
    unique_words = extractor.extract_words(sample_text)
    print(unique_words)