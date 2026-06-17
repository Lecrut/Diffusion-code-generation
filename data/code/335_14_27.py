class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    test_sentence = "Hello world This is a production ready script"
    tokens = processor.tokenize(test_sentence)
    assert len(tokens) > 0 and isinstance(tokens, list), "Tokenization failed"