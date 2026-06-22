class SquareAreaCalculator:
    @staticmethod
    def calculate_area(side_length):
        return side_length ** 2

    @staticmethod
    def sum_areas(side1, side2):
        area1 = SquareAreaCalculator.calculate_area(side1)
        area2 = SquareAreaCalculator.calculate_area(side2)
        return area1 + area2

if __name__ == '__main__':
    result = SquareAreaCalculator.sum_areas(5, 3)
    print(result)