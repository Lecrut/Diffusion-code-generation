import string

class PunctuationExtractor:
    def __init__(self):
        self.punctuation_set = set(string.punctuation)

    def extract(self, text):
        return [char for char in text if char in self.punctuation_set]

if __name__ == '__main__':
    extractor = PunctuationExtractor()
    sample_text = "Hello, world! How are you?"
    print(extractor.extract(sample_text))