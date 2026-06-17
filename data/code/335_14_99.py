import re
class NLPProcessor:
    def tokenize(self, sentence):
        return [token for token in re.findall(r'\S+', sentence)]
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello world! This is a test."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)