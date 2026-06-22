class LeapYearCalculator:
    def days_remaining_in_february(self, year):
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return 29 if is_leap_year else 28

if __name__ == '__main__':
    calculator = LeapYearCalculator()
    year = 2023
    print(calculator.days_remaining_in_february(year))