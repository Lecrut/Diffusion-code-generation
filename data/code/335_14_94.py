class SentenceTokenizer:
    def tokenize(self, sentence):
        return sentence.split()
if __name__ == '__main__':
    tokenizer = SentenceTokenizer()
    sample_sentence = "Hello world! This is a test."
    tokens = tokenizer.tokenize(sample_sentence)
    print(tokens)