class WeightCalculator:
    def __init__(self):
        self.weights = set()

    def add_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        self.weights.add(weight)

    def calculate_weight_difference(self, weight1, weight2):
        if weight1 not in self.weights or weight2 not in self.weights:
            raise ValueError("Both weights must be added to the calculator first")
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    weight1 = 60.4
    weight2 = 58.9
    calculator.add_weight(weight1)
    calculator.add_weight(weight2)
    difference = calculator.calculate_weight_difference(weight1, weight2)
    print(difference)