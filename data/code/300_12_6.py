class MonthDays:
    FEBRUARY = 2
    MONTHS_WITH_30_DAYS = {4, 6, 9, 11}
    MONTHS_WITH_31_DAYS = {1, 3, 5, 7, 8, 10, 12}

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @classmethod
    def days_in_month(cls, year, month):
        if month == cls.FEBRUARY:
            return 29 if cls.is_leap_year(year) else 28
        elif month in cls.MONTHS_WITH_30_DAYS:
            return 30
        else:
            return 31

if __name__ == '__main__':
    print(MonthDays.days_in_month(2023, 2))
    print(MonthDays.days_in_month(2024, 2))
    print(MonthDays.days_in_month(2023, 4))