import re
class NLPProcessor:
    @staticmethod
    def tokenize(sentence):
        return [token for token in sentence.split() if len(token) > 1]
if __name__ == '__main__':
    sample_sentence = "Natural language processing is a fascinating field."
    tokens = NLPProcessor.tokenize(sample_sentence)
    print(tokens)