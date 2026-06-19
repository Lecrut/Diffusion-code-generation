class SquareCalculator:
    @staticmethod
    def calculate_square_area(side):
        return side * side

if __name__ == '__main__':
    sample_side_length = 7
    area_result = SquareCalculator.calculate_square_area(sample_side_length)
    print(area_result)