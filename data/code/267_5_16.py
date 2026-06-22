class WordAnalyzer:
    def __init__(self, min_length=10):
        self.min_length = min_length

    def is_long_word(self, word):
        return len(word) > self.min_length

if __name__ == '__main__':
    analyzer = WordAnalyzer()
    sample_words = ["short", "longerword", "thisisalongword", "medium", "verylongwordexample"]
    for word in sample_words:
        print(analyzer.is_long_word(word))