class PunctuationExtractor:
    def __init__(self):
        self.punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    def extract_punctuation(self, text):
        return [char for char in text if char in self.punctuation and not char.isalnum()]

if __name__ == '__main__':
    extractor = PunctuationExtractor()
    sample_string = "Hello, world! How are you? This is a test."
    result = extractor.extract_punctuation(sample_string)
    print(result)