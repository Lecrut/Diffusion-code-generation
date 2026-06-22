class WordChecker:
    def __init__(self, min_length):
        self.min_length = min_length

    def is_word_long(self, word):
        return len(word) > self.min_length

if __name__ == '__main__':
    checker = WordChecker(5)
    test_words = ["short", "longerword"]
    results = [checker.is_word_long(word) for word in test_words]
    for i, word in enumerate(test_words):
        print(f"Is '{word}' long (min length 5): {results[i]}")