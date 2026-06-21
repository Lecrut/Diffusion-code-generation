import re

class WordExtractor:
    PUNCTUATION = r'[^\w\s]'
    
    @staticmethod
    def extract_words(text):
        cleaned_text = re.sub(WordExtractor.PUNCTUATION, '', text)
        words = set(re.findall(r'\b\w+\b', cleaned_text.lower()))
        return list(words)

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, world, and hello again."
    extractor = WordExtractor()
    result = extractor.extract_words(sample_string)
    print(result)