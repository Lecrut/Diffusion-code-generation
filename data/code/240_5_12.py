class SquareAreaCalculator:
    @staticmethod
    def calculate_area(side):
        return side * side

if __name__ == '__main__':
    sample_side = 4
    area = SquareAreaCalculator.calculate_area(sample_side)
    print(f"Side: {sample_side}, Area: {area}")