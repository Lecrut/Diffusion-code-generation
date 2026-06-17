class NLPProcessor:
    def tokenize(self, sentence):
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Natural language processing is a subfield of linguistics."
    tokens = NLPProcessor().tokenize(sample_sentence)
    print(tokens)