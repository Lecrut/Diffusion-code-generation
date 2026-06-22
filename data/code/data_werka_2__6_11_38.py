class WeightCalculator:
    def __init__(self, weights):
        self.weights = weights

    def calculate_difference(self):
        weight1, weight2 = self.weights.values()
        return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weights = {'weight1': 80.0, 'weight2': 72.5}
    calculator = WeightCalculator(sample_weights)
    difference = calculator.calculate_difference()
    print(difference)