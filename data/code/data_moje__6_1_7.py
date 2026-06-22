class WeightCalculator:
    def __init__(self, unit="kg"):
        self.unit = unit

    def calculate_difference(self, weight_a, weight_b):
        if weight_a < 0 or weight_b < 0:
            raise ValueError("Weights cannot be negative")
        return abs(weight_a - weight_b)

if __name__ == "__main__":
    calculator = WeightCalculator("kg")
    weight_one = 150.5
    weight_two = 120.2
    difference = calculator.calculate_difference(weight_one, weight_two)
    print(difference)