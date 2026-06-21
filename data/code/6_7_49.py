class WeightCalculator:
    def __init__(self):
        self.weights = {}

    def add_weight(self, identifier, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        self.weights[identifier] = weight

    def calculate_weight_difference(self, id1, id2):
        if id1 not in self.weights or id2 not in self.weights:
            raise ValueError("Both weights must be added to the calculator first")
        return abs(self.weights[id1] - self.weights[id2])

if __name__ == '__main__':
    calculator = WeightCalculator()
    weight_id_1 = 'Alice'
    weight_id_2 = 'Bob'
    weight_value_1 = 65.3
    weight_value_2 = 72.8
    calculator.add_weight(weight_id_1, weight_value_1)
    calculator.add_weight(weight_id_2, weight_value_2)
    difference = calculator.calculate_weight_difference(weight_id_1, weight_id_2)
    print(difference)