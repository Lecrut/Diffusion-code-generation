class WeightCalculator:
    def __init__(self):
        self.weights = {}

    def add_weight(self, name, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        self.weights[name] = weight

    def calculate_weight_difference(self, name1, name2):
        if name1 not in self.weights or name2 not in self.weights:
            raise ValueError("Both weights must be added to the calculator first")
        return abs(self.weights[name1] - self.weights[name2])

if __name__ == '__main__':
    calculator = WeightCalculator()
    weight1_name = "Alice"
    weight2_name = "Bob"
    weight1_value = 65.3
    weight2_value = 70.9

    calculator.add_weight(weight1_name, weight1_value)
    calculator.add_weight(weight2_name, weight2_value)

    difference = calculator.calculate_weight_difference(weight1_name, weight2_name)
    print(difference)