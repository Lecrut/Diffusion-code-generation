class LeapYearCalculator:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_remaining_in_february(self):
        if self.is_leap_year():
            return 29
        else:
            return 28

if __name__ == '__main__':
    calculator = LeapYearCalculator(2023)
    print(calculator.days_remaining_in_february())