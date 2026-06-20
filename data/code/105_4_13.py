import datetime

class DateUtils:
    TARGET_DATE = datetime.date(2023, 11, 1)

    @staticmethod
    def nearest_saturday(date_obj):
        days_until_saturday = (5 - date_obj.weekday()) % 7
        return date_obj + datetime.timedelta(days=days_until_saturday)

if __name__ == '__main__':
    target_date = DateUtils.TARGET_DATE
    next_saturday = DateUtils.nearest_saturday(target_date)
    print(f"Target Date: {target_date}")
    print(f"Nearest Saturday: {next_saturday}")