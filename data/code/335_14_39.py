import re
class NLPProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return [token for token in sentence.split() if len(token.strip()) > 0]
if __name__ == '__main__':
    sample_sentence = "Natural language processing is a fascinating field of study."
    result = NLPProcessor.tokenize(sample_sentence)
    print(result)