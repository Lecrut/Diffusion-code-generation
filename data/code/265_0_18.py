class EvenIndexCharExtractor:
    def extract_chars(self, phrase):
        return ''.join(char for index, char in enumerate(phrase) if index % 2 == 0)

if __name__ == '__main__':
    extractor = EvenIndexCharExtractor()
    sample_phrase = "Hello, World!"
    extracted_chars = extractor.extract_chars(sample_phrase)
    print(extracted_chars)