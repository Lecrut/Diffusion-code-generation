class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    test_sentence = "Hello world from Python."
    tokens = processor.tokenize(test_sentence)
    assert isinstance(tokens, list), "Result must be a list"
    print(f"{tokens}")