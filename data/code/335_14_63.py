import re
class NLPProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return [token for token in re.findall(r'\S+', sentence)]
if __name__ == '__main__':
    sample_sentence = "Natural language processing is an interdisciplinary field."
    result = NLPProcessor.tokenize(sample_sentence)
    print(result)