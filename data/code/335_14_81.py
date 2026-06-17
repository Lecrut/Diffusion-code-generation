import re
class NLPProcessor:
    def tokenize(self, sentence):
        return [word.strip() for word in sentence.split()] if sentence else []
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Natural language processing is a fascinating field."
    result = processor.tokenize(sample_sentence)
    print(result)