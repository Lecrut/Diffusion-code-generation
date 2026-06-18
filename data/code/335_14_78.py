import re
class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        if not isinstance(sentence, str):
            raise TypeError("Input must be a string.")
        tokens = re.findall(r'\b\w+\b', sentence)
        return tokens
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello, world! This is a test."
    result = processor.tokenize(sample_sentence)
    print(result)