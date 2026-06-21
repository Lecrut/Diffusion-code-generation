import re

class WordTokenizer:
    def __init__(self):
        self.pattern = r'\b\w+\b'

    def tokenize(self, text):
        return re.findall(self.pattern, text)

if __name__ == '__main__':
    tokenizer = WordTokenizer()
    sample_string = "This is a sample string with various words and punctuation! How about this?"
    words = tokenizer.tokenize(sample_string)
    print(words)