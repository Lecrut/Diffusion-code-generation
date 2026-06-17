import re
class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return [token for token in sentence.split() if token]
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello world this is a test of the tokenizer."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)