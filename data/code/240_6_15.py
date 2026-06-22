class SquareAreaCalculator:
    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    sample_side = 5.0
    area = SquareAreaCalculator.calculate_area(sample_side)
    print(f"The side of the square is: {sample_side}")
    print(f"The area of the square is: {area}")