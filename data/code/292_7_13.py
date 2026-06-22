class EllipsePerimeterCalculator:
    @staticmethod
    def calculate_perimeter(a, b):
        h = ((a - b) ** 2) / ((a + b) ** 2)
        return (a + b) * (1 + (3 * h) / (10 + (4 - 3 * h) ** 0.5))

if __name__ == '__main__':
    calculator = EllipsePerimeterCalculator()
    perimeter1 = calculator.calculate_perimeter(3, 4)
    print(f"Perimeter for ellipse with semi-major axis 3 and semi-minor axis 4: {perimeter1}")
    perimeter2 = calculator.calculate_perimeter(10, 20)
    print(f"Perimeter for ellipse with semi-major axis 10 and semi-minor axis 20: {perimeter2}")