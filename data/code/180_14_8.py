class WordChecker:
    def __init__(self, text):
        self._words = self._tokenize(text)
    def _tokenize(self, text):
        return [word.lower() for word in text.split()]
    def contains_word(self, word):
        return word.lower() in self._words
if __name__ == '__main__':
    sample_text = "This is a sample sentence for testing word presence."
    checker = WordChecker(sample_text)
    word1 = "sample"
    word2 = "testing"
    word3 = "python"
    word4 = "missing"
    print(f"Does the text contain '{word1}'? {checker.contains_word(word1)}")
    print(f"Does the text contain '{word2}'? {checker.contains_word(word2)}")
    print(f"Does the text contain '{word3}'? {checker.contains_word(word3)}")
    print(f"Does the text contain '{word4}'? {checker.contains_word(word4)}")