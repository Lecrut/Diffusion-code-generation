class TextAnalyzer:
    def find_all_words(self, text):
        words = text.lower().split()
        unique_words = set(word for word in words if word.isalpha())
        return sorted(list(unique_words))
if __name__ == '__main__':
    analyzer = TextAnalyzer()
    sample_text = "This is a sample text for word analysis. Words like this are important and unique."
    result = analyzer.find_all_words(sample_text)
    print(result)