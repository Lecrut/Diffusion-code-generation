class LeapYearCalculator:
    LEAP_YEAR_DAYS = 29
    COMMON_YEAR_DAYS = 28

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def days_in_february(cls, year):
        if cls.is_leap_year(year):
            return cls.LEAP_YEAR_DAYS
        else:
            return cls.COMMON_YEAR_DAYS

if __name__ == '__main__':
    sample_year = 2024
    result = LeapYearCalculator.days_in_february(sample_year)
    print(result)