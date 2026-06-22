class SquareAreaCalculator:
    @staticmethod
    def calculate_area(side_length):
        return side_length ** 2

if __name__ == '__main__':
    test_side = 12
    area = SquareAreaCalculator.calculate_area(test_side)
    print(f"The area of a square with side {test_side} is: {area}")