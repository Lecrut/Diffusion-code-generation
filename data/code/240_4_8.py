class SquareAreaCalculator:
    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    sample_side = 7
    result_area = SquareAreaCalculator.calculate_area(sample_side)
    print(result_area)