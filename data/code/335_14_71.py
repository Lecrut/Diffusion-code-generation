import re
class NLPProcessor:
    def __init__(self):
        self.compiled_regex = re.compile(r'\s+')
    def tokenize(self, sentence: str) -> list[str]:
        if not isinstance(sentence, str):
            raise TypeError("Input must be a string")
        tokens = [word for word in sentence.split() if len(word.strip()) > 0]
        return tokens
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello, world! This is an example."
    result_tokens = processor.tokenize(sample_sentence)
    print(result_tokens)