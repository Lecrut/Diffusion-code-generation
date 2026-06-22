class WordFrequencyAnalyzer:

    def __init__(self):
        self.frequency = {}

    def process_text(self, text):
        words = text.lower().split()
        for word in words:
            self.frequency[word] = self.frequency.get(word, 0) + 1

    def get_frequency(self, word):
        return self.frequency.get(word, 0)
if __name__ == '__main__':
    analyzer = WordFrequencyAnalyzer()
    sample_text = 'Hello world hello Python python'
    analyzer.process_text(sample_text)
    print(analyzer.get_frequency('hello'))
    print(analyzer.get_frequency('python'))
    print(analyzer.get_frequency('world'))