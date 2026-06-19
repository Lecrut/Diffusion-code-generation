class TriangleCalculator:
    ORIGIN_X = 0
    ORIGIN_Y = 0

    @staticmethod
    def calculate_area(x, y):
        return abs(0.5 * (x * TriangleCalculator.ORIGIN_Y + y * TriangleCalculator.ORIGIN_X - 
                           TriangleCalculator.ORIGIN_Y * x - TriangleCalculator.ORIGIN_X * y))

if __name__ == '__main__':
    sample_x = 7
    sample_y = 24
    area = TriangleCalculator.calculate_area(sample_x, sample_y)
    print(area)