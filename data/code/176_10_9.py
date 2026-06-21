import re

class WordExtractor:
    def extract_words(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    extractor = WordExtractor()
    sample_text1 = "This is a test string with words."
    print(extractor.extract_words(sample_text1))
    
    sample_text2 = "Hello, this is another example sentence for word extraction."
    print(extractor.extract_words(sample_text2))