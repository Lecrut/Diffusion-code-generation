class SquareAreaCalculator:
    def __init__(self, side_length: float):
        if not isinstance(side_length, (int, float)) or side_length < 0:
            raise ValueError("Side length must be a non-negative number")
        self.side_length = side_length

    def calculate_area(self) -> float:
        return float(self.side_length ** 2)

if __name__ == '__main__':
    calculator1 = SquareAreaCalculator(5.0)
    area1 = calculator1.calculate_area()
    print(f"The area of the square with side length {calculator1.side_length} is {area1}")

    calculator2 = SquareAreaCalculator(10.5)
    area2 = calculator2.calculate_area()
    print(f"The area of the square with side length {calculator2.side_length} is {area2}")