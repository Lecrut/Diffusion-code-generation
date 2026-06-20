class DateUtil:
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    @staticmethod
    def adjust_february_days(year):
        if DateUtil.is_leap_year(year):
            DateUtil.days_in_month[2] = 29
        else:
            DateUtil.days_in_month[2] = 28

    @classmethod
    def calculate_day_of_year(cls, month, day):
        cls.adjust_february_days(2023)
        day_of_year = sum(cls.days_in_month[:month]) + day
        return day_of_year
if __name__ == '__main__':
    result1 = DateUtil.calculate_day_of_year(1, 1)
    print(f'Day of Year: {result1}')
    result2 = DateUtil.calculate_day_of_year(3, 15)
    print(f'Day of Year: {result2}')
    result3 = DateUtil.calculate_day_of_year(12, 25)
    print(f'Day of Year: {result3}')