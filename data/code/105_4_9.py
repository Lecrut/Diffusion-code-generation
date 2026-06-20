import datetime

class DateHelper:
    @staticmethod
    def nearest_saturday(date_obj):
        days_until_saturday = (5 - date_obj.weekday()) % 7
        return date_obj + datetime.timedelta(days=days_until_saturday)

if __name__ == '__main__':
    start_date = datetime.date(2023, 11, 1)
    nearest_sat = DateHelper.nearest_saturday(start_date)
    print(f"Nearest Saturday to {start_date}: {nearest_sat}")