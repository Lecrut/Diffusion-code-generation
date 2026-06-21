import re

class TextTokenizer:
    TOKEN_PATTERN = r'\b\w+\b'

    @staticmethod
    def tokenize(sentence):
        return re.findall(TextTokenizer.TOKEN_PATTERN, sentence)

if __name__ == '__main__':
    tokenizer = TextTokenizer()
    sample_sentence = "Hello world! This is a test sentence with numbers 123."
    result = tokenizer.tokenize(sample_sentence)
    print(result)