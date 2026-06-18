import re
class NLPProcessor:
    def __init__(self):
        self._token_pattern = re.compile(r'\S+')
    def tokenize(self, sentence: str) -> list[str]:
        return [word for word in re.findall(self._token_pattern, sentence)]
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello, world! This is a test."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)