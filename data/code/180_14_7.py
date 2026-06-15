class WordPresenceChecker:
    def __init__(self, text):
        self._text = text.lower()
        self._words = set(text.lower().split())
    def contains_word(self, word):
        return word in self._words
if __name__ == '__main__':
    sample_text = "This is a sample text for checking word presence in an object oriented manner"
    checker = WordPresenceChecker(sample_text)
    word1 = "sample"
    word2 = "word"
    word3 = "python"
    word4 = "missing"
    print(f"Does the text contain '{word1}'? {checker.contains_word(word1)}")
    print(f"Does the text contain '{word2}'? {checker.contains_word(word2)}")
    print(f"Does the text contain '{word3}'? {checker.contains_word(word3)}")
    print(f"Does the text contain '{word4}'? {checker.contains_word(word4)}")