class WordPresenceChecker:
    def __init__(self, text):
        self._text = text.lower()
    def contains_word(self, word):
        return word in self._text
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    checker = WordPresenceChecker(sample_text)
    word1 = "fox"
    word2 = "cat"
    word3 = "dog"
    print(f"Does the text contain '{word1}'? {checker.contains_word(word1)}")
    print(f"Does the text contain '{word2}'? {checker.contains_word(word2)}")
    print(f"Does the text contain '{word3}'? {checker.contains_word(word3)}")