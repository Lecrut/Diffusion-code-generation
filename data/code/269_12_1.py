class PunctuationAnalyzer:
    def analyze(self, text):
        counts = {}
        for char in text:
            if char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
                counts[char] = counts.get(char, 0) + 1
        return counts
if __name__ == '__main__':
    analyzer = PunctuationAnalyzer()
    sample_text = "Hello world! How are you today? This is a test, isn't it?"
    result = analyzer.analyze(sample_text)
    print(result)