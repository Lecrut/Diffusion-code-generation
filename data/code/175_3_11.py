class WordExtractor:
    DELIMITERS = r'\s+|[,.!?;:]'
    
    @staticmethod
    def extract_words(text):
        words = [word for word in re.split(WordExtractor.DELIMITERS, text) if word]
        return words

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_string1 = "Hello world! This is a test, with various spaces and punctuation."
    print(extractor.extract_words(sample_string1))