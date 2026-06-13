class WordPresenceChecker:
    def __init__(self, text):
        self._text = text
    def contains_word(self, word):
        return word in self._text
if __name__ == '__main__':
    sample_text = "This is a sample text for checking word presence."
    checker = WordPresenceChecker(sample_text)
    word1 = "sample"
    word2 = "text"
    word3 = "python"
    print(f"Does the text contain '{word1}'? {checker.contains_word(word1)}")
    print(f"Does the text contain '{word2}'? {checker.contains_word(word2)}")
    print(f"Does the text contain '{word3}'? {checker.contains_word(word3)}")