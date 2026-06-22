class WeightCalculator:
    MIN_WEIGHT = 0.0
    MAX_WEIGHT = 300.0

    @staticmethod
    def validate_weight(weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        if weight < WeightCalculator.MIN_WEIGHT or weight > WeightCalculator.MAX_WEIGHT:
            raise ValueError(f"Weight must be between {WeightCalculator.MIN_WEIGHT} and {WeightCalculator.MAX_WEIGHT}")

    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        WeightCalculator.validate_weight(weight)
        self.weights.append(weight)

    def calculate_weight_difference(self, weight1, weight2):
        if weight1 not in self.weights or weight2 not in self.weights:
            raise ValueError("Both weights must be added to the calculator first")
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    weight1 = 65.3
    weight2 = 70.9
    calculator.add_weight(weight1)
    calculator.add_weight(weight2)
    difference = calculator.calculate_weight_difference(weight1, weight2)
    print(difference)