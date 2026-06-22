class WordAnalyzer:
    def __init__(self, min_length=15):
        self.min_length = min_length

    def is_word_long(self, word):
        return len(word) > self.min_length

if __name__ == '__main__':
    analyzer = WordAnalyzer()
    print(analyzer.is_word_long("short"))
    print(analyzer.is_word_long("thisisalongword"))
    print(analyzer.is_word_long("a_very_long_string_example"))
    print(analyzer.is_word_long("exactlyfifteen"))
    print(analyzer.is_word_long(""))