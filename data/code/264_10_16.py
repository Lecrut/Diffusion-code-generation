class TextAnalyzer:
    def __init__(self):
        self.frequency = {}

    def analyze(self, text):
        words = text.lower().split()
        for word in words:
            self.frequency[word] = self.frequency.get(word, 0) + 1

    def get_frequency(self):
        return self.frequency

if __name__ == '__main__':
    analyzer = TextAnalyzer()
    sample_text = "Hello world hello Python python"
    analyzer.analyze(sample_text)
    print(analyzer.get_frequency())