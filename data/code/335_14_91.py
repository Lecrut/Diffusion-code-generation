class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "This is a production-ready tokenizer example."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)