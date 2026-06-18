import re
class NLPProcessor:
    def tokenize(self, sentence):
        return [token for token in re.findall(r'\S+', sentence)]
if __name__ == '__main__':
    sample_sentence = "Hello world! This is a test case."
    processor = NLPProcessor()
    tokens = processor.tokenize(sample_sentence)
    print(tokens)