class WordLengthChecker:
    def __init__(self, threshold=10):
        self.threshold = threshold

    def is_long_word(self, word):
        return len(word) > self.threshold

if __name__ == '__main__':
    checker = WordLengthChecker()
    sample_words = ["short", "thisisalongword", "anotherword", "verylongwordexample"]
    for word in sample_words:
        print(f"{word}: {checker.is_long_word(word)}")