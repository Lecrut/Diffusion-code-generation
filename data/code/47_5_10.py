class TriangleCalculator:
    def __init__(self):
        self.results = []

    def calculate_area(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        area = 0.5 * base * height
        self.results.append(area)
        return area

if __name__ == '__main__':
    calculator = TriangleCalculator()
    try:
        print(calculator.calculate_area(3, 4))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print(calculator.calculate_area(0, 5))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print(calculator.calculate_area(-1, 2))
    except ValueError as e:
        print(f"Error: {e}")