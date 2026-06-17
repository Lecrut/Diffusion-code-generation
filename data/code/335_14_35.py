class NLPProcessor:
    def tokenize(self, sentence):
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    test_sentence = "Hello world this is a sample sentence."
    tokens = processor.tokenize(test_sentence)
    print(tokens)