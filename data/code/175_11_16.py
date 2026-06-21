import re

class WordExtractor:
    def extract_words(self, text):
        return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    extractor = WordExtractor()
    long_text = "this is a very long sentence, designed to test the efficiency of word splitting on extremely long strings! Ensure that the time complexity and space usage are minimal for large inputs."
    words = extractor.extract_words(long_text)
    print(words)