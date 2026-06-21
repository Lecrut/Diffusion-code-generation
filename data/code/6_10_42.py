class WeightDiffCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def validate_weights(self):
        if not (isinstance(self.weight1, (int, float)) and isinstance(self.weight2, (int, float))):
            raise ValueError("Both weights must be numbers.")

    def compute_difference(self):
        self.validate_weights()
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    weight_calculator = WeightDiffCalculator(88.5, 73.9)
    difference = weight_calculator.compute_difference()
    print(difference)