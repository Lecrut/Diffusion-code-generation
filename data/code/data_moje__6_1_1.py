class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    calc = WeightCalculator(10.5, 5.2)
    result = calc.calculate_difference()
    print(result)