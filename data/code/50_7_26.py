class AreaCalculator:
    def get_difference(self, area_a, area_b):
        if not isinstance(area_a, (int, float)) or not isinstance(area_b, (int, float)):
            raise ValueError("Both areas must be numbers")
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    result = calculator.get_difference(10.5, 7.2)
    print(result)