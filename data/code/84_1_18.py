class DateCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, month):
        if month == 2:
            return 29 if self.is_leap_year(self.year) else 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def calculate_day_of_year(self):
        cumulative_days = 0
        for m in range(1, self.month):
            cumulative_days += self.days_in_month(m)
        cumulative_days += self.day
        return cumulative_days

if __name__ == '__main__':
    calculator1 = DateCalculator(2023, 10, 26)
    print(calculator1.calculate_day_of_year())

    calculator2 = DateCalculator(2024, 1, 1)
    print(calculator2.calculate_day_of_year())

    calculator3 = DateCalculator(2000, 2, 29)
    print(calculator3.calculate_day_of_year())

    calculator4 = DateCalculator(2023, 12, 31)
    print(calculator4.calculate_day_of_year())

    calculator5 = DateCalculator(2023, 1, 1)
    print(calculator5.calculate_day_of_year())

    calculator6 = DateCalculator(2023, 3, 1)
    print(calculator6.calculate_day_of_year())