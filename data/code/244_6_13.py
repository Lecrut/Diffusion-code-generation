class RhombusAreaCalculator:
    DIAGONAL_1_FIRST = 6
    DIAGONAL_2_FIRST = 8
    DIAGONAL_1_SECOND = 10
    DIAGONAL_2_SECOND = 12

    @staticmethod
    def calculate_area(diagonal1, diagonal2):
        return (diagonal1 * diagonal2) / 2

    @classmethod
    def calculate_total_area(cls):
        area_first = cls.calculate_area(cls.DIAGONAL_1_FIRST, cls.DIAGONAL_2_FIRST)
        area_second = cls.calculate_area(cls.DIAGONAL_1_SECOND, cls.DIAGONAL_2_SECOND)
        return area_first + area_second

if __name__ == '__main__':
    total_area = RhombusAreaCalculator.calculate_total_area()
    print(total_area)