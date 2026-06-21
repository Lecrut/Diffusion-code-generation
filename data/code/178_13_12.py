import re

class SentenceProcessor:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def extract_words(self):
        return re.findall(r'\b\w+\b', self.phrase)

if __name__ == '__main__':
    processor = SentenceProcessor("This is a complex example phrase with various words and punctuation!")
    words = processor.extract_words()
    print(words)