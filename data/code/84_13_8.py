class DateUtils:
    MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
    MONTHS_WITH_30_DAYS = [4, 6, 9, 11]

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def days_in_month(month, year):
        if month in DateUtils.MONTHS_WITH_31_DAYS:
            return 31
        elif month in DateUtils.MONTHS_WITH_30_DAYS:
            return 30
        else:
            return 29 if DateUtils.is_leap_year(year) else 28

    @staticmethod
    def day_of_year(year, month, day):
        days = sum(DateUtils.days_in_month(m, year) for m in range(1, month)) + day
        return days

if __name__ == '__main__':
    print(DateUtils.day_of_year(2023, 4, 15))