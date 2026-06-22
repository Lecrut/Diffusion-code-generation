class WeightCalculator:
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
    sample_weights = [10.5, 20.3, 30.7, 40.2, 50.8]
    calculator = WeightCalculator(sample_weights)
    difference = calculator.calculate_difference()
    print(difference)