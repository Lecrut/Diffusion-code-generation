class YearCalculator:
    def find_difference(self, year1: int, year2: int) -> int:
        return abs(year1 - year2)
if __name__ == '__main__':
    calculator = YearCalculator()
    year_a = 2023
    year_b = 1990
    difference = calculator.find_difference(year_a, year_b)
    print(f"The difference between {year_a} and {year_b} is: {difference}")