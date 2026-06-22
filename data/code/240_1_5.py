class SquareAreaCalculator:
    @staticmethod
    def calculate_area(side_length: int) -> int:
        return side_length * side_length

if __name__ == '__main__':
    calculator = SquareAreaCalculator()
    side1 = 5
    area1 = calculator.calculate_area(side1)
    print(f"The area of a square with side {side1} is: {area1}")
    side2 = 10
    area2 = calculator.calculate_area(side2)
    print(f"The area of a square with side {side2} is: {area2}")