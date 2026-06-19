class WeightCalculator:

    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)
if __name__ == '__main__':
    weight_calculator = WeightCalculator(70.5, 65.2)
    difference = weight_calculator.calculate_difference()
    print(difference)