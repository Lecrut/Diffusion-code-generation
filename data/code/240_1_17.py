class SquareCalculator:
    @staticmethod
    def calculate_area(side: int) -> int:
        return side * side

if __name__ == '__main__':
    calculator = SquareCalculator()
    area1 = calculator.calculate_area(5)
    print(f"The area of a square with side 5 is: {area1}")