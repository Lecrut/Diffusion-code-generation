class FebruaryDaysCalculator:
    MONTH_DAYS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    LEAP_YEAR_MONTH_DAYS = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def days_in_february(cls, year):
        if cls.is_leap_year(year):
            return cls.LEAP_YEAR_MONTH_DAYS[2]
        else:
            return cls.MONTH_DAYS[2]

if __name__ == '__main__':
    year = 2023
    print(FebruaryDaysCalculator.days_in_february(year))