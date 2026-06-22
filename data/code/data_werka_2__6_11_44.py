class WeightAnalyzer:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def get_weights(self):
        return self.weight1, self.weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    analyzer = WeightAnalyzer(70.0, 65.8)
    weights = analyzer.get_weights()
    difference = analyzer.calculate_difference()
    print(f"Weights: {weights}")
    print(f"Difference: {difference}")