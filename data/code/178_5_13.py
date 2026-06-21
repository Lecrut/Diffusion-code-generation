import re

class WordExtractor:
    NON_ALNUM_PATTERN = re.compile('[^a-zA-Z0-9\\s]+')

    @staticmethod
    def extract_words(text):
        cleaned_text = WordExtractor.NON_ALNUM_PATTERN.sub('', text)
        words = cleaned_text.split()
        return [word.lower() for word in words]
if __name__ == '__main__':
    sample_string = 'Hello, world! This is a test string with some punctuation and numbers 123.'
    extractor = WordExtractor()
    result = extractor.extract_words(sample_string)
    print(result)