class WeightCalculator:
    def calculate_difference(self, weight1, weight2):
        if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
            raise ValueError("Both weights must be numbers")
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    weight1 = 70.5
    weight2 = 65.3
    difference = calculator.calculate_difference(weight1, weight2)
    print(difference)