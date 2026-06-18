import re
class NLPProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return re.findall(r'\S+', sentence.lower())
if __name__ == '__main__':
    sample_sentence = "Hello, this is a production-ready tokenization example."
    result = NLPProcessor.tokenize(sample_sentence)
    print(result)