class WeightCalculator:
    def __init__(self):
        self.weights = {}

    def add_weight(self, label, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        self.weights[label] = weight

    def calculate_weight_difference(self, label1, label2):
        if label1 not in self.weights or label2 not in self.weights:
            raise ValueError("Both weights must be added to the calculator first")
        return abs(self.weights[label1] - self.weights[label2])

if __name__ == '__main__':
    calculator = WeightCalculator()
    calculator.add_weight('weight1', 70.5)
    calculator.add_weight('weight2', 68.3)
    difference = calculator.calculate_weight_difference('weight1', 'weight2')
    print(difference)