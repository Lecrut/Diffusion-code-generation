class WeightCalculator:
    def __init__(self):
        self.weights = {}

    def set_weight(self, name, weight):
        self.weights[name] = weight

    def calculate_difference(self, name1, name2):
        if name1 not in self.weights or name2 not in self.weights:
            raise ValueError("One or both weights are not set.")
        return abs(self.weights[name1] - self.weights[name2])

if __name__ == '__main__':
    calculator = WeightCalculator()
    calculator.set_weight('Alice', 70.5)
    calculator.set_weight('Bob', 68.3)
    difference = calculator.calculate_difference('Alice', 'Bob')
    print(difference)