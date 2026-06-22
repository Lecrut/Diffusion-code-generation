class LengthAnalyzer:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def find_min_max(self):
        return min(self.length1, self.length2), max(self.length1, self.length2)

    def calculate_ratio(self):
        minimum, maximum = self.find_min_max()
        return maximum / minimum

if __name__ == '__main__':
    a = 7
    b = 21
    analyzer = LengthAnalyzer(a, b)
    min_length, max_length = analyzer.find_min_max()
    ratio = analyzer.calculate_ratio()
    print(f"Minimum length: {min_length}")
    print(f"Maximum length: {max_length}")
    print(f"Ratio of larger to smaller length: {ratio}")