from datetime import date, timedelta

class MonthUtils:
    @staticmethod
    def days_in_month(year, month):
        if month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            return 29 if is_leap else 28
        elif month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        else:
            return 30

    @staticmethod
    def days_left_in_month():
        today = date.today()
        _, last_day = MonthUtils.days_in_month(today.year, today.month)
        last_day_of_month = date(today.year, today.month, last_day)
        return (last_day_of_month - today).days

if __name__ == '__main__':
    print(MonthUtils.days_left_in_month())