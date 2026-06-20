import datetime

class DateValidator:
    WEEKDAY_THRESHOLD = 5

    @staticmethod
    def is_weekday(date_string):
        try:
            date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            return date_obj.weekday() < DateValidator.WEEKDAY_THRESHOLD
        except ValueError:
            return False

if __name__ == '__main__':
    checker = DateValidator()
    dates_to_check = ["2023-10-25", "2023-10-26", "2023-10-27", "2023-10-28", "2023-10-29", "2023/10/25"]
    for date in dates_to_check:
        print(f"Is {date} a weekday? {checker.is_weekday(date)}")