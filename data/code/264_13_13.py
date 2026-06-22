class WordFrequencyAnalyzer:
    def __init__(self):
        self.word_count = {}

    def update(self, text):
        words = text.split()
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1

    def most_frequent_word(self):
        return max(self.word_count.items(), key=lambda x: x[1])

if __name__ == '__main__':
    analyzer = WordFrequencyAnalyzer()
    sample_text = "hello world hello python programming is fun and exciting"
    analyzer.update(sample_text)
    most_frequent, count = analyzer.most_frequent_word()
    print(f"The most frequent word is '{most_frequent}' with a count of {count}")