import re

class WordExtractor:
    WORD_PATTERN = r'\b\w+\b'

    @staticmethod
    def extract_words(phrase):
        return re.findall(WordExtractor.WORD_PATTERN, phrase)

if __name__ == '__main__':
    input_phrase = "This is a complex example phrase with various words and punctuation!"
    extracted_words = WordExtractor.extract_words(input_phrase)
    print(extracted_words)