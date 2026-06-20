class YearCalculator:
    @staticmethod
    def calculate_difference(year1: int, year2: int) -> int:
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearCalculator()
    difference = calculator.calculate_difference(2023, 1990)
    print(difference)