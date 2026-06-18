import re
class NLPProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return [word for word in sentence.split() if len(word.strip()) > 0]
if __name__ == '__main__':
    sample_sentence = "Natural language processing is the study of computational linguistics."
    result = NLPProcessor.tokenize(sample_sentence)
    print(result)