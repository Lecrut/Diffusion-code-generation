import sys
class NLPProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "This is a production-ready tokenization example."
    tokens = NLPProcessor.tokenize(sample_sentence)
    print(tokens)