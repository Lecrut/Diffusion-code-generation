class DateCalculator:
    MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    LEAP_MONTH_DAYS = 29

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    @classmethod
    def update_month_days(cls, year):
        if cls.is_leap_year(year):
            cls.MONTHS[1] = cls.LEAP_MONTH_DAYS
        else:
            cls.MONTHS[1] = 28

    @staticmethod
    def calculate_day_of_year(year, month, day):
        DateCalculator.update_month_days(year)
        return sum(DateCalculator.MONTHS[:month - 1]) + day

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 4
    sample_day = 15
    result = DateCalculator.calculate_day_of_year(sample_year, sample_month, sample_day)
    print(result)