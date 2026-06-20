class YearCalculator:
    def __init__(self, year1: int, year2: int):
        self.year1 = year1
        self.year2 = year2

    def calculate_difference(self) -> int:
        return abs(self.year1 - self.year2)

if __name__ == '__main__':
    calculator1 = YearCalculator(2023, 1990)
    print(calculator1.calculate_difference())

    calculator2 = YearCalculator(2000, 2024)
    print(calculator2.calculate_difference())

    calculator3 = YearCalculator(1850, 1850)
    print(calculator3.calculate_difference())