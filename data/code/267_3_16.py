class WordAnalyzer:
    def __init__(self, length_threshold=5):
        self.length_threshold = length_threshold
    
    def is_word_long(self, word):
        return len(word) > self.length_threshold

if __name__ == '__main__':
    analyzer = WordAnalyzer(7)
    print(analyzer.is_word_long("example"))
    print(analyzer.is_word_long("hi"))