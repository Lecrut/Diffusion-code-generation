class CharacterAnalyzer:
    def analyze(self, text):
        counts = {}
        for char in text:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        return counts
if __name__ == '__main__':
    analyzer = CharacterAnalyzer()
    sample_string = "hello world"
    result = analyzer.analyze(sample_string)
    print(result)