class LengthAnalyzer:
    def __init__(self, len1, len2):
        self.len1 = len1
        self.len2 = len2

    def analyze(self):
        min_len = min(self.len1, self.len2)
        max_len = max(self.len1, self.len2)
        diff = abs(self.len1 - self.len2)
        return (min_len, max_len, diff)

if __name__ == '__main__':
    length_analyzer = LengthAnalyzer(15.7, 22.3)
    result = length_analyzer.analyze()
    print(result)