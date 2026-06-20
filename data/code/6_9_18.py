class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = float(weight1)
        self.weight2 = float(weight2)

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

    def set_weights(self, weight1, weight2):
        self.weight1 = float(weight1)
        self.weight2 = float(weight2)

    def get_weight1(self):
        return self.weight1

    def get_weight2(self):
        return self.weight2

if __name__ == '__main__':
    calculator = WeightCalculator(10.5, 7.3)
    difference = calculator.calculate_difference()
    print(difference)

    calculator.set_weights(20.0, 15.5)
    new_difference = calculator.calculate_difference()
    print(new_difference)