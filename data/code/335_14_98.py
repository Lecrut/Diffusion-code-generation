import re
class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return re.findall(r'\S+', sentence.strip())
if __name__ == '__main__':
    sample_sentence = "Hello world! This is a test."
    tokens = NLPProcessor().tokenize(sample_sentence)
    print(tokens)