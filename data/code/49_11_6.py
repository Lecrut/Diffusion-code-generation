class LengthAnalyzer:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def get_lengths(self):
        return {'length1': self.length1, 'length2': self.length2}

    def calculate_difference(self):
        return abs(self.length1 - self.length2)

    def calculate_ratio(self):
        return max(self.length1, self.length2) / min(self.length1, self.length2)

    def analyze(self):
        result = {
            'original_length1': self.length1,
            'original_length2': self.length2,
            'difference': self.calculate_difference(),
            'ratio': self.calculate_ratio()
        }
        return result

if __name__ == '__main__':
    sample_length1 = 20
    sample_length2 = 8
    analyzer = LengthAnalyzer(sample_length1, sample_length2)
    
    print(analyzer.get_lengths())
    print("Difference:", analyzer.calculate_difference())
    print("Ratio:", analyzer.calculate_ratio())
    print("Analysis Result:", analyzer.analyze())