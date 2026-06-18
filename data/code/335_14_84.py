import sys
class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split() if sentence else []
if __name__ == '__main__':
    sample = "Hello world from Python."
    processor = NLPProcessor()
    result = processor.tokenize(sample)
    print(result)
    sys.exit(0)