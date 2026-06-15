class WordPresenceChecker:
    def __init__(self, text):
        self._words = self._tokenize(text)
    def _tokenize(self, text):
        import re
        return set(re.findall(r'\b\w+\b', text.lower()))
    def contains_word(self, word):
        return word in self._words
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is clever."
    checker = WordPresenceChecker(sample_text)
    words_to_check = ["fox", "dog", "cat", "jumps"]
    print("Checking word presence:")
    for word in words_to_check:
        if checker.contains_word(word):
            print(f"'{word}': Present")
        else:
            print(f"'{word}': Not Present")