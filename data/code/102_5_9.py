import datetime

class DateChecker:
    WEEKDAYS = range(5)

    @staticmethod
    def is_weekday(date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return date_obj.weekday() in DateChecker.WEEKDAYS
        except ValueError:
            return False

if __name__ == '__main__':
    dates = ["2023-10-27", "2024-02-29", "2023-10-28", "2023-02-28"]
    results = [DateChecker.is_weekday(date) for date in dates]
    print(results)