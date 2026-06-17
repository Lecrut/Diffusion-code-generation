import re
class NLPProcessor:
    def tokenize(self, sentence):
        return [token for token in sentence.split() if token]
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello world! This is a test."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)