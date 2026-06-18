import re
class NLPProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    sample_sentence = "Hello, this is a test of the natural language processing capabilities."
    tokens = NLPProcessor.tokenize(sample_sentence)
    print(tokens)