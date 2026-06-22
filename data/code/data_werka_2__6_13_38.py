def calculate_absolute_difference(weight1, weight2):
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise ValueError("Both weights must be numbers.")
    return abs(weight1 - weight2)

class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return calculate_absolute_difference(self.weight1, self.weight2)

if __name__ == '__main__':
    sample_weight1 = 70.5
    sample_weight2 = 65.3
    calculator = WeightCalculator(sample_weight1, sample_weight2)
    difference = calculator.calculate_difference()
    print(difference)