class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    test_sentence = "Hello world this is a sample sentence for tokenization."
    tokens = processor.tokenize(test_sentence)
    print(tokens)