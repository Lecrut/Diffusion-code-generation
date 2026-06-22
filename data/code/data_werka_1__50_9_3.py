class AreaCalculator:
    def get_difference(self, area_a, area_b):
        if not (isinstance(area_a, (int, float)) and isinstance(area_b, (int, float))):
            raise ValueError("Both areas must be numbers.")
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    try:
        area1 = 50.34
        area2 = 20.78
        difference = calculator.get_difference(area1, area2)
        print(f"The positive difference is: {difference:.2f}")
    except ValueError as e:
        print(e)