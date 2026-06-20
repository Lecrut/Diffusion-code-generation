class WeightCalculator:
    def __init__(self, weight1, weight2):
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise TypeError("Weights must be numeric")
        self.weight1 = weight1
        self.weight2 = weight2

    def get_weight1(self):
        return self.weight1

    def get_weight2(self):
        return self.weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    calculator = WeightCalculator(100.5, 75.2)
    result = calculator.calculate_difference()
    print(result)