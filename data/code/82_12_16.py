class YearGapCalculator:
    def calculate_gap(self, year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearGapCalculator()
    year_a = 2023
    year_b = 1998
    gap = calculator.calculate_gap(year_a, year_b)
    print(gap)