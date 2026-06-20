import datetime

class DateChecker:
    WEEKDAY_RANGE = range(0, 5)
    
    @staticmethod
    def is_weekday(date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            weekday = date_obj.weekday()
            return weekday in DateChecker.WEEKDAY_RANGE
        except ValueError:
            return False

if __name__ == '__main__':
    dates = ["2023-10-27", "2024-02-29", "2023-11-01", "2023-02-28"]
    weekday_dates = [date for date in dates if DateChecker.is_weekday(date)]
    print(f"Weekday dates: {weekday_dates}")