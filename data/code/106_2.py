class TimeCalculator:
    def calculate_year_difference(self, year1: int, year2: int) -> int:
        return abs(year1 - year2)
if __name__ == '__main__':
    calculator = TimeCalculator()
    date1 = 2000
    date2 = 2020
    difference = calculator.calculate_year_difference(date1, date2)
    print(difference)