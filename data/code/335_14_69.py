import sys
class NLPSentenceProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world, this is a test."
    result = NLPSentenceProcessor.tokenize(sample_sentence)
    print(result)