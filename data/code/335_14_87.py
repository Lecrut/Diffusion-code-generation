import re
class NLPProcessor:
    def tokenize(self, sentence):
        return [token for token in re.findall(r'\S+', sentence)]
if __name__ == '__main__':
    sample_sentence = "Natural language processing is a fascinating field."
    result = NLPProcessor().tokenize(sample_sentence)
    print(result)