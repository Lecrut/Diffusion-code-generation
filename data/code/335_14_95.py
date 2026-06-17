import re
class NLPProcessor:
    def tokenize(self, sentence):
        return re.findall(r'\S+', sentence)
if __name__ == '__main__':
    sample = "Natural language processing is a fascinating field."
    result = NLPProcessor().tokenize(sample)
    print(result)