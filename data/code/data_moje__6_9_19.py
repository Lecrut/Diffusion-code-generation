class WeightCalculator:
    def __init__(self, unit="kg"):
        self.unit = unit
        self.weights = {}

    def set_weight(self, name, value):
        self.weights[name] = value

    def get_weight(self, name):
        return self.weights.get(name)

    def calculate_difference(self, name_a, name_b):
        weight_a = self.weights.get(name_a)
        weight_b = self.weights.get(name_b)
        if weight_a is None or weight_b is None:
            raise ValueError("One or both weights are not defined")
        return weight_a - weight_b

if __name__ == '__main__':
    calculator = WeightCalculator()
    calculator.set_weight("box_a", 50.0)
    calculator.set_weight("box_b", 30.0)
    diff = calculator.calculate_difference("box_a", "box_b")
    print(diff)
    calculator.set_weight("box_c", 45.0)
    diff2 = calculator.calculate_difference("box_b", "box_c")
    print(diff2)