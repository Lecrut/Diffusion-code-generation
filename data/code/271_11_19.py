class TextAnalyzer:
    def __init__(self):
        self.frequency_dict = {}

    def analyze(self, text):
        for char in text:
            if char != ' ':
                if char in self.frequency_dict:
                    self.frequency_dict[char] += 1
                else:
                    self.frequency_dict[char] = 1

    def get_frequencies(self):
        return self.frequency_dict

if __name__ == '__main__':
    analyzer = TextAnalyzer()
    sample_text = "Hello, World! This is a test."
    analyzer.analyze(sample_text)
    frequencies = analyzer.get_frequencies()
    print(frequencies)