import re
class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return [word for word in self._clean(sentence)]
    @staticmethod
    def _clean(text: str) -> list[str]:
        text = ' '.join(str(word).strip() for word in re.findall(r'\S+', text))
        if not text.strip():
            return []
        words = [w for w in text.split(' ') if w]
        return words
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Natural Language Processing is the study of computational linguistics."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)