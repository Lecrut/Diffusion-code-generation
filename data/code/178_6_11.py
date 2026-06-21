import re

class WordExtractor:
    MIN_WORD_LENGTH = 2
    
    @staticmethod
    def extract_words(sentence):
        pattern = r'\b\w+\b'
        words = re.findall(pattern, sentence)
        return [word for word in words if len(word) >= WordExtractor.MIN_WORD_LENGTH]
    
if __name__ == '__main__':
    extractor = WordExtractor()
    sample_sentence = "This is a test sentence with some short and longer words."
    extracted_words = extractor.extract_words(sample_sentence)
    print(extracted_words)