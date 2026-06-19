class LengthAnalyzer:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def get_lengths(self):
        return {
            'length1': self.length1,
            'length2': self.length2,
            'difference': abs(self.length1 - self.length2),
            'ratio': max(self.length1, self.length2) / min(self.length1, self.length2)
        }

if __name__ == '__main__':
    sample_length1 = 7
    sample_length2 = 21
    analyzer = LengthAnalyzer(sample_length1, sample_length2)
    result = analyzer.get_lengths()
    print(result)