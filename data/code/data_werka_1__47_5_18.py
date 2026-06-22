class TriangleCalculator:

    def __init__(self):
        self.results = []

    def calculate_area(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError('Base and height must be positive numbers.')
        area = 0.5 * base * height
        self.results.append(area)
        return area
if __name__ == '__main__':
    calculator = TriangleCalculator()
    try:
        area1 = calculator.calculate_area(3, 4)
        print(f'Area for base 3, height 4: {area1}')
    except ValueError as e:
        print(f'Error: {e}')
    try:
        area2 = calculator.calculate_area(5, 6)
        print(f'Area for base 5, height 6: {area2}')
    except ValueError as e:
        print(f'Error: {e}')
    try:
        area3 = calculator.calculate_area(-1, 4)
        print(f'Area for base -1, height 4: {area3}')
    except ValueError as e:
        print(f'Error: {e}')