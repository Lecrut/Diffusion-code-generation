import re

class UniqueWordExtractor:
    def __init__(self):
        self.seen_words = set()

    def extract_unique_words(self, text):
        words = re.findall(r'\b\w+\b', text)
        unique_words = []
        for word in words:
            if word.lower() not in self.seen_words:
                unique_words.append(word)
                self.seen_words.add(word.lower())
        return unique_words

if __name__ == '__main__':
    extractor = UniqueWordExtractor()
    sample_string = "Hello World! This is a test string with numbers 123 and punctuation."
    result = extractor.extract_unique_words(sample_string)
    print(result)