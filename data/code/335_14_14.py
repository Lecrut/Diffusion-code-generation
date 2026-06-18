import re
class NLPProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return [token for token in sentence.split() if token]
if __name__ == '__main__':
    sample_sentence = "Natural language processing is the study of computational linguistics."
    result = NLPProcessor.tokenize(sample_sentence)
    print(result)