import re
class NLPProcessor:
    def tokenize(self, sentence):
        return [token for token in self._clean_and_split(sentence)] if isinstance(sentence, str) else []
    @staticmethod
    def _clean_and_split(text):
        text = ' '.join(str(token).strip() for token in re.findall(r'\S+', text))
        tokens = text.split(' ')
        return [token for token in tokens if len(token) > 0]
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Hello, world! This is a test sentence."
    result = processor.tokenize(sample_sentence)
    print(result)