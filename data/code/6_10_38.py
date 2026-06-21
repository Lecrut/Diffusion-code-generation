class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def compute_difference(self):
        if not (isinstance(self.weight1, (int, float)) and isinstance(self.weight2, (int, float))):
            raise ValueError("Both weights must be numbers.")
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    weight_calculator = WeightCalculator(90.7, 85.4)
    difference = weight_calculator.compute_difference()
    print(difference)