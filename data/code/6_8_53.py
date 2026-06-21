class WeightAnalyzer:
    def __init__(self, weights):
        if not weights:
            raise ValueError("The list of weights cannot be empty.")
        self.weights = weights

    def find_extremes(self):
        return max(self.weights), min(self.weights)

    def calculate_difference(self):
        max_weight, min_weight = self.find_extremes()
        return max_weight - min_weight

if __name__ == '__main__':
    sample_weights = [10.5, 20.3, 5.8, 40.9, 25.6]
    analyzer = WeightAnalyzer(sample_weights)
    difference = analyzer.calculate_difference()
    print(difference)