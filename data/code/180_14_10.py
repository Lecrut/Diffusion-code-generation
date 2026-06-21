class WordPresenceChecker:
    def __init__(self, text):
        self._words = set(text.lower().split())

    def contains_word(self, word):
        return word.lower() in self._words

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