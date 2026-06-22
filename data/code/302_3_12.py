class MonthDaysCalculator:
    FEBRUARY = 2
    DAYS_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def days_in_month(cls, year):
        month_days = cls.DAYS_IN_MONTHS[:]
        if cls.is_leap_year(year):
            month_days[cls.FEBRUARY] += 1
        return dict(enumerate(month_days, start=1))

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    print(calculator.days_in_month(2024))
    print(calculator.days_in_month(2023))