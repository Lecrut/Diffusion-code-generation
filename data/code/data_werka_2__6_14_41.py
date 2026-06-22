class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def validate_weights(self):
        if self.weight1 < 0 or self.weight2 < 0:
            raise ValueError("Weights cannot be negative")
        return True

    def compute_difference(self):
        if not self.validate_weights():
            return None
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    weight_calculator = WeightCalculator(15.5, 10.2)
    try:
        difference = weight_calculator.compute_difference()
        print(difference)
    except ValueError as e:
        print(e)