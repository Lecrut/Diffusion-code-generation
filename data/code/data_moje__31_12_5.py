class SquareCalculator:
    SHAPE_NAME = "square"

    @staticmethod
    def compute_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    side = 7
    area = SquareCalculator.compute_area(side)
    print(area)