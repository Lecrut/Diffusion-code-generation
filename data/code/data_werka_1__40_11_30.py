class FirstLetterExtractor:
    def extract_all(self, words):
        first_letters = []
        for word in words:
            if word:
                first_letters.append(word[0])
        return first_letters

if __name__ == '__main__':
    sample_words = ["kiwi", "lemon", "mango"]
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(sample_words)
    print(result)