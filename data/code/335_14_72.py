import re
class NLPProcessor:
    def tokenize(self, sentence):
        return [word for word in sentence.split() if not re.match(r'^\s+$', ' ') and len(word) > 0]
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello world! This is a test."
    result = processor.tokenize(sample_sentence)
    print(result)