class AreaCalculator:
    def calculate_difference(self, area1, area2):
        return abs(area1 - area2)

if __name__ == '__main__':
    calculator = AreaCalculator()
    result = calculator.calculate_difference(75.3, 30.8)
    print(result)