import re
class WordExtractor:
    def extract_words(self, text):
        return re.findall(r'\b\w+\b', text)
if __name__ == '__main__':
    extractor = WordExtractor()
    sample_text = "This is a sample sentence for word extraction using regular expressions."
    words = extractor.extract_words(sample_text)
    print(words)