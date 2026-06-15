class PunctuationExtractor:
    def extract(self, text):
        punctuation = []
        for char in text:
            if char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
                punctuation.append(char)
        return punctuation
if __name__ == '__main__':
    extractor = PunctuationExtractor()
    sample_text = "Hello world! How are you, and what is your favorite color? It's blue."
    extracted_punctuation = extractor.extract(sample_text)
    print(extracted_punctuation)