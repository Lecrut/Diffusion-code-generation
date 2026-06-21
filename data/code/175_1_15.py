import re

class Tokenizer:
    TOKEN_PATTERN = re.compile(r'\b\w+\b')

    @staticmethod
    def tokenize(sentence):
        return Tokenizer.TOKEN_PATTERN.findall(sentence)

if __name__ == '__main__':
    sample_sentence = "Hello world! This is a test sentence, 123."
    result = Tokenizer.tokenize(sample_sentence)
    print(result)