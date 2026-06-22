class WeightComparison:
    def __init__(self, weights):
        self.weights = weights

    def calculate_difference(self):
        if len(self.weights) != 2:
            raise ValueError("Exactly two weights are required.")
        return abs(self.weights['Alice'] - self.weights['Bob'])

if __name__ == '__main__':
    sample_weights = {'Alice': 75.5, 'Bob': 68.3}
    comparison = WeightComparison(sample_weights)
    difference = comparison.calculate_difference()
    print(difference)