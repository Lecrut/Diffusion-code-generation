class NLPProcessor:
    def tokenize(self, sentence):
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "This is a production-ready optimized tokenizer."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)