class TextAnalyzer:
    def __init__(self):
        self.word_count = {}

    def process_text(self, text):
        words = text.split()
        for word in words:
            self.word_count[word] = self.word_count.get(word, 0) + 1

    def get_most_frequent_word(self):
        return max(self.word_count.items(), key=lambda x: x[1])

if __name__ == '__main__':
    analyzer = TextAnalyzer()
    sample_text = "hello world hello python programming is fun and exciting"
    analyzer.process_text(sample_text)
    most_frequent, count = analyzer.get_most_frequent_word()
    print(f"The most frequent word is '{most_frequent}' with a count of {count}")