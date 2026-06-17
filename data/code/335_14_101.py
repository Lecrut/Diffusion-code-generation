import re
class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return [token.strip() for token in sentence.split()] if sentence else []
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello world, this is a test."
    result = processor.tokenize(sample_sentence)
    print(result)