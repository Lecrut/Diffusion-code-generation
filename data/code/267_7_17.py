class WordAnalyzer:

    def __init__(self, max_length):
        self.max_length = max_length

    def is_long(self, word):
        return len(word) > self.max_length
if __name__ == '__main__':
    analyzer = WordAnalyzer(10)
    print(analyzer.is_long('short'))
    print(analyzer.is_long('this is too long'))