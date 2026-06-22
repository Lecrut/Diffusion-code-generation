class SquareAreaCalculator:
    @staticmethod
    def compute_area(side_length: int) -> int:
        return side_length * side_length

if __name__ == '__main__':
    calculator = SquareAreaCalculator()
    sample_side1 = 5
    area1 = calculator.compute_area(sample_side1)
    print(f"The area of a square with side {sample_side1} is: {area1}")

    sample_side2 = 10
    area2 = calculator.compute_area(sample_side2)
    print(f"The area of a square with side {sample_side2} is: {area2}")