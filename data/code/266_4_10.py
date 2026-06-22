class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def count_unique_words(self):
        words = self.text.split()
        unique_words = set(words)
        return len(unique_words)

if __name__ == '__main__':
    analyzer1 = TextAnalyzer("hello world hello Python")
    print(analyzer1.count_unique_words())

    analyzer2 = TextAnalyzer("hello world hello")
    print(analyzer2.count_unique_words())

    analyzer3 = TextAnalyzer("Python programming is fun and educational")
    print(analyzer3.count_unique_words())

    analyzer4 = TextAnalyzer("hello world hello python programming")
    print(analyzer4.count_unique_words())