class SentenceAnalyzer:
    def __init__(self, sentence):
        self.sentence = sentence

    def filter_long_words(self):
        return [word for word in self.sentence.split() if len(word) > 3]

if __name__ == '__main__':
    analyzer = SentenceAnalyzer("The quick brown fox jumps over the lazy dog")
    long_words = analyzer.filter_long_words()
    print(long_words)