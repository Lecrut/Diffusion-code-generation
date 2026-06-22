class AreaCalculator:
    def calculate_difference(self, area1, area2):
        if not (isinstance(area1, (int, float)) and isinstance(area2, (int, float))):
            raise ValueError("Both areas must be numbers.")
        return abs(area1 - area2)

if __name__ == '__main__':
    calculator = AreaCalculator()
    a = 90.5
    b = 47.8
    result = calculator.calculate_difference(a, b)
    print(result)