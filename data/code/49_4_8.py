class LengthAnalyzer:
    def __init__(self, len1, len2):
        self.len1 = len1
        self.len2 = len2

    def find_min_max(self):
        return min(self.len1, self.len2), max(self.len1, self.len2)

    def calculate_ratio(self):
        minimum, maximum = self.find_min_max()
        return maximum / minimum

if __name__ == '__main__':
    length_a = 7
    length_b = 28
    analyzer = LengthAnalyzer(length_a, length_b)
    ratio = analyzer.calculate_ratio()
    print(ratio)