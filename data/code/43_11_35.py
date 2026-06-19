class SquareCalculator:
    @staticmethod
    def calculate_square_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    sample_values = [4.0, 6.5, 12]
    for value in sample_values:
        print(SquareCalculator.calculate_square_area(value))