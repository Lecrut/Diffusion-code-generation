class WordExtractor:
    def __init__(self, phrase):
        self.phrase = phrase

    def extract_words(self):
        return [word for word in self.phrase.split(',') if word]

if __name__ == '__main__':
    extractor = WordExtractor("apple,banana,,orange,,,,")
    print(extractor.extract_words())