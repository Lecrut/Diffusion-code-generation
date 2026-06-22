from datetime import datetime

class DateChecker:
    HOLIDAYS = ["2023-10-12"]

    @staticmethod
    def is_weekend(date_str):
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            weekday = date_obj.weekday()
            return weekday >= 5
        except ValueError:
            return False

    @staticmethod
    def is_holiday(date_str):
        return date_str in DateChecker.HOLIDAYS

if __name__ == '__main__':
    sample_date = "2023-10-12"
    print(DateChecker.is_weekend(sample_date))
    print(DateChecker.is_holiday(sample_date))