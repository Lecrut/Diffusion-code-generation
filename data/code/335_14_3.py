import re
class NLPProcessor:
    def tokenize(self, sentence):
        return [word for word in self._preprocess(sentence)]
    @staticmethod
    def _preprocess(s):
        s = s.strip()
        if not s:
            return []
        tokens = re.findall(r'\b\w+\b', s)
        return tokens
if __name__ == '__main__':
    processor = NLPProcessor()
    sentence = "Hello, world! This is a test."
    result = processor.tokenize(sentence)
    print(result)