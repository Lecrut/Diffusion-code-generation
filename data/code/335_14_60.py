import re
class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return [token for token in re.findall(r'\S+', sentence)]
if __name__ == '__main__':
    sample_sentence = "Hello world! This is a test."
    result = NLPProcessor().tokenize(sample_sentence)
    print(result)