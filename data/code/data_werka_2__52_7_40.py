class TriangleAreaCalculator:
    ORIGIN_X = 0
    ORIGIN_Y = 0

    @staticmethod
    def calculate_area(x, y):
        return abs(0.5 * (TriangleAreaCalculator.ORIGIN_X * y - x * TriangleAreaCalculator.ORIGIN_Y))

if __name__ == '__main__':
    sample_x = 3
    sample_y = 4
    area = TriangleAreaCalculator.calculate_area(sample_x, sample_y)
    print(area)