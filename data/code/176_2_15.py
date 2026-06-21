import re

class WordTokenizer:
    TOKEN_PATTERN = r'\b\w+\b'

    @staticmethod
    def tokenize(text):
        return re.findall(WordTokenizer.TOKEN_PATTERN, text)

if __name__ == '__main__':
    sample_string = "This is a sample string with various words and punctuation! How about this?"
    tokenizer = WordTokenizer()
    words = tokenizer.tokenize(sample_string)
    print(words)