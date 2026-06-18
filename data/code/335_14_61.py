import re
class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return [token for token in self._split(sentence)]
    @staticmethod
    def _split(text: str) -> list[str]:
        text = ' '.join(text.split()) if isinstance(text, str) else ''
        tokens = re.findall(r'\S+', text)
        return tokens
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello world! This is a test sentence."
    result_tokens = processor.tokenize(sample_sentence)
    print(result_tokens)