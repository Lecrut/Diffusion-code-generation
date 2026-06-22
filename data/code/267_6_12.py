class WordChecker:
    def __init__(self, threshold=10):
        self.threshold = threshold

    def is_long_word(self, word):
        return len(word) > self.threshold

if __name__ == '__main__':
    checker = WordChecker(12)
    words = ["short", "thisisalongword", "anotherword", "verylongwordexample"]
    for word in words:
        print(f"Is '{word}' long? {checker.is_long_word(word)}")