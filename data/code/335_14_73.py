import re
class NLPProcessor:
    def tokenize(self, sentence):
        return [word for word in sentence.split() if len(word) > 1]
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello world! This is a test."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)