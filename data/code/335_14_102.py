class NLPProcessor:
    def tokenize(self, sentence):
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world this is a test of the natural language processing system"
    result = NLPProcessor().tokenize(sample_sentence)
    print(result)