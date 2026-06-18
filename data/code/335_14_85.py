import re
class NLPProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return [token for token in sentence.split() if len(token.strip()) > 0]
if __name__ == '__main__':
    sample_sentence = "This is a test of the natural language processing capabilities."
    result = NLPProcessor.tokenize(sample_sentence)
    print(result)