class WordChecker:
    def __init__(self, text):
        self._text = text.lower()
        self._words = self._tokenize(self._text)
    def _tokenize(self, text):
        return [word for word in text.split() if word]
    def contains_word(self, word):
        return word in self._words
if __name__ == '__main__':
    sample_text = "This is a sample sentence for word checking."
    checker = WordChecker(sample_text)
    word1 = "sample"
    word2 = "sentence"
    word3 = "missing"
    print(f"Does the text contain '{word1}'? {checker.contains_word(word1)}")
    print(f"Does the text contain '{word2}'? {checker.contains_word(word2)}")
    print(f"Does the text contain '{word3}'? {checker.contains_word(word3)}")