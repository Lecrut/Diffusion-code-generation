class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello world this is a test of tokenization."
    result = processor.tokenize(sample_sentence)
    print(result)