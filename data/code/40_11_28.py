class FirstLetterExtractor:
    def extract_all(self, words):
        return [word[0] for word in words if word]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_words = ["apple", "banana", "cherry"]
    first_letters = extractor.extract_all(sample_words)
    print(first_letters)