class LeapYearCalculator:
    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_february(self, year):
        if self.is_leap_year(year):
            return 29
        else:
            return 28

if __name__ == '__main__':
    calculator = LeapYearCalculator()
    sample_year = 2024
    print(calculator.days_in_february(sample_year))