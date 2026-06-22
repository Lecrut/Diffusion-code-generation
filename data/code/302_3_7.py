class MonthDays:
    FEBRUARY = 28

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def days_in_month(cls, year):
        months = {
            1: 31, 2: cls.FEBRUARY, 3: 31,
            4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31
        }
        months[2] += cls.is_leap_year(year)
        return months

if __name__ == '__main__':
    print(MonthDays.days_in_month(2024))
    print(MonthDays.days_in_month(2023))