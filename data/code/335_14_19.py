import sys
class NLPProcessor:
    def tokenize(self, sentence):
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello world! This is a test."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)