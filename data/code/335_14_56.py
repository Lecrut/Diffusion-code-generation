class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello world this is a test of the tokenizer functionality."
    tokens = processor.tokenize(sample_sentence)
    assert len(tokens) > 0 and isinstance(tokens, list), "Tokenization failed"