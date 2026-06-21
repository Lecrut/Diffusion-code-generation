class WeightDifferenceCalculator:
    def __init__(self, weights):
        if not all(isinstance(w, (int, float)) for w in weights):
            raise ValueError("All weights must be numbers.")
        self.weights = sorted(weights)

    def compute_difference(self):
        return abs(self.weights[1] - self.weights[0])

if __name__ == '__main__':
    sample_weights = {'weight1': 72.5, 'weight2': 69.8}
    weights_list = list(sample_weights.values())
    calculator = WeightDifferenceCalculator(weights_list)
    difference = calculator.compute_difference()
    print(difference)