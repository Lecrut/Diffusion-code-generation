class WeightAnalyzer:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

    def heavier_weight(self):
        return max(self.weight1, self.weight2)

if __name__ == '__main__':
    weight_analyzer = WeightAnalyzer(70.0, 75.3)
    difference = weight_analyzer.calculate_difference()
    print(f"Difference: {difference}")
    heavier = weight_analyzer.heavier_weight()
    print(f"Heavier Weight: {heavier}")