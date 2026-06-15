class TextAnalyzer:
    def find_all_words(self, text):
        words = text.lower().split()
        unique_words = set(words)
        sorted_words = sorted(list(unique_words))
        return sorted_words
if __name__ == '__main__':
    analyzer = TextAnalyzer()
    sample_text = "The quick brown fox jumps over the lazy dog. Fox and dog are friends."
    result = analyzer.find_all_words(sample_text)
    print(result)