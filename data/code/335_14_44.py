import sys
class NLPProcessor:
    @staticmethod
    def tokenize(sentence):
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Natural language processing is a fascinating field."
    tokens = NLPProcessor.tokenize(sample_sentence)
    print(tokens)