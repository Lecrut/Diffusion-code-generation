class YearCalculator:
    @staticmethod
    def calculate_difference(y1: int, y2: int) -> int:
        return abs(y1 - y2)

if __name__ == '__main__':
    year_a = 2023
    year_b = 1985
    difference = YearCalculator.calculate_difference(year_a, year_b)
    print(difference)