import re
class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return re.findall(r'\S+', sentence.strip())
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Natural language processing is a fascinating field."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)