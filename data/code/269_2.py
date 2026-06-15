class PunctuationExtractor:
    def extract(self, text):
        punctuation = []
        for char in text:
            if char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
                punctuation.append(char)
        return punctuation
if __name__ == '__main__':
    extractor = PunctuationExtractor()
    sample_text = "Hello world! How are you today? This is a test, isn't it?"
    extracted_punctuation = extractor.extract(sample_text)
    print(extracted_punctuation)