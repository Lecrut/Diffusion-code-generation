class DateCalculator:
    def __init__(self):
        self.months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def adjust_february_days(self, year):
        if self.is_leap_year(year):
            self.months[1] = 29
        else:
            self.months[1] = 28

    def calculate_day_of_year(self, year, month, day):
        self.adjust_february_days(year)
        return sum(self.months[:month - 1]) + day

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.calculate_day_of_year(2023, 4, 15)
    print(result)