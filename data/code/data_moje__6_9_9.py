class WeightCalculator:
    def calculate_difference(self, weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    w1 = 10.5
    w2 = 7.2
    diff = calculator.calculate_difference(w1, w2)
    print(diff)