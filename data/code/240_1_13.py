class SquareAreaCalculator:
    @staticmethod
    def calculate_area(side_length: int) -> int:
        return side_length * side_length

if __name__ == '__main__':
    calculator = SquareAreaCalculator()
    print(f"The area of a square with side 5 is: {calculator.calculate_area(5)}")
    print(f"The area of a square with side 10 is: {calculator.calculate_area(10)}")
    print(f"The area of a square with side 3 is: {calculator.calculate_area(3)}")