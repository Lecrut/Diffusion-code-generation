class AreaCalculator:
    def calculate_difference(self, area1, area2):
        if not isinstance(area1, (int, float)) or not isinstance(area2, (int, float)):
            raise ValueError("Both areas must be numbers")
        return abs(area1 - area2)

if __name__ == '__main__':
    calculator = AreaCalculator()
    area1 = 50.5
    area2 = 30.2
    difference = calculator.calculate_difference(area1, area2)
    print(difference)