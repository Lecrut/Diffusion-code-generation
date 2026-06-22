class WeightDifferenceCalculator:
    def __init__(self, weight1, weight2):
        if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
            raise ValueError("Both weights must be numbers.")
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    try:
        sample_weights = {'Alice': 85.0, 'Bob': 79.2}
        calculator = WeightDifferenceCalculator(sample_weights['Alice'], sample_weights['Bob'])
        difference = calculator.calculate_difference()
        print(f"Weight Difference: {difference}")
    except ValueError as e:
        print(e)