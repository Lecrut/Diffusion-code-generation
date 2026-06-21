class WeightCalculator:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        self.weights.append(weight)

    def _validate_weights_existence(self, weight1, weight2):
        if weight1 not in self.weights:
            raise ValueError(f"Weight {weight1} is not added to the calculator.")
        if weight2 not in self.weights:
            raise ValueError(f"Weight {weight2} is not added to the calculator.")

    def calculate_weight_difference(self, weight1, weight2):
        self._validate_weights_existence(weight1, weight2)
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    weight1 = 60.3
    weight2 = 58.9
    calculator.add_weight(weight1)
    calculator.add_weight(weight2)
    difference = calculator.calculate_weight_difference(weight1, weight2)
    print(f"The weight difference is: {difference}")