class YearCalculator:
    def find_absolute_difference(self, year1, year2):
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearCalculator()
    years1 = 10
    years2 = 5
    difference = calculator.find_absolute_difference(years1, years2)
    print(f"Absolute Difference between {years1} and {years2}: {difference}")