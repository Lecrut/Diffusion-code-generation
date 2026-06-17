class NlpProcessor:
    def tokenize(self, sentence):
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world this is a production ready tokenizer"
    tokens = NlpProcessor().tokenize(sample_sentence)
    print(tokens)