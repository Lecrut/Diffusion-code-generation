class LengthAnalyzer:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def validate_lengths(self):
        if not (isinstance(self.length1, (int, float)) and isinstance(self.length2, (int, float))):
            raise ValueError("Both lengths must be numbers.")
        if self.length1 <= 0 or self.length2 <= 0:
            raise ValueError("Lengths must be positive.")

    def calculate_ratio(self):
        self.validate_lengths()
        minimum = min(self.length1, self.length2)
        maximum = max(self.length1, self.length2)
        ratio = maximum / minimum
        return ratio

if __name__ == '__main__':
    try:
        analyzer = LengthAnalyzer(10, 25)
        ratio = analyzer.calculate_ratio()
        print(ratio)
    except ValueError as e:
        print(e)