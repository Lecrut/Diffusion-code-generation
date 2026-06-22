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
    s1 = 5
    s2 = 3
    result = SquareAreaCalculator.sum_areas(s1, s2)
    print(result)