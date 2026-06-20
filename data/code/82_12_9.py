class YearGapCalculator:
    def calculate_gap(self, year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearGapCalculator()
    start_year = 2023
    end_year = 1985
    gap = calculator.calculate_gap(start_year, end_year)
    print(gap)