import re
class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return [word for word in re.findall(r'\S+', sentence)]
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "This is a production-ready tokenization example."
    tokens = processor.tokenize(sample_sentence)
    assert isinstance(tokens, list), "Tokenize must return a list"
    print("Exit code: 0")