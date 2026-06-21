import re

class WordExtractor:
    WORD_PATTERN = r'\b\w+\b'

    @staticmethod
    def extract_words(sentence):
        return re.findall(WordExtractor.WORD_PATTERN, sentence)

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence for testing purposes."
    extracted_words = WordExtractor.extract_words(sample_sentence)
    print(extracted_words)