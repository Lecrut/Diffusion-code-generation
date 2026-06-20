class WeightCalculator:
    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        self.weights.append(weight)

    def calculate_difference(self, weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    w1 = 50.5
    w2 = 30.2
    calculator.add_weight(w1)
    calculator.add_weight(w2)
    result = calculator.calculate_difference(w1, w2)
    print(result)