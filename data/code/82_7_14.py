class YearCalculator:
    def find_absolute_difference(self, year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearCalculator()
    sample_year1 = 2030
    sample_year2 = 1985
    difference = calculator.find_absolute_difference(sample_year1, sample_year2)
    print(f"Absolute difference between {sample_year1} and {sample_year2}: {difference}")