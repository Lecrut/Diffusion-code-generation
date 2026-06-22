class WeightAnalyzer:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

    def heavier_weight(self):
        return max(self.weight1, self.weight2)

if __name__ == '__main__':
    analyzer = WeightAnalyzer(70.2, 65.8)
    difference = analyzer.calculate_difference()
    heavier = analyzer.heavier_weight()
    print(f"Difference: {difference}")
    print(f"Heavier weight: {heavier}")