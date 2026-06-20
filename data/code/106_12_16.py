from datetime import date

class DateCalculator:
    DAYS_PER_YEAR = 365

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def days_in_year(year: int) -> int:
        return DateCalculator.DAYS_PER_YEAR + 1 if DateCalculator.is_leap_year(year) else DateCalculator.DAYS_PER_YEAR

    @classmethod
    def years_between_dates(cls, date1: date, date2: date) -> float:
        year1, month1, day1 = date1.year, date1.month, date1.day
        year2, month2, day2 = date2.year, date2.month, date2.day

        days_diff = 0
        if year1 < year2:
            for year in range(year1 + 1, year2):
                days_diff += cls.days_in_year(year)
        elif year1 > year2:
            for year in range(year2, year1):
                days_diff -= cls.days_in_year(year)

        days_diff += (date1 - date(year1, month1, day1)).days
        if year1 == year2:
            days_diff += (date(year2, month2, day2) - date2).days

        return abs(days_diff / cls.DAYS_PER_YEAR)

if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = date(2020, 3, 1)
    date_b = date(1995, 8, 15)
    difference = calculator.years_between_dates(date_a, date_b)
    print(difference)