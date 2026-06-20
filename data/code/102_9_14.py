import datetime

class DateChecker:
    def __init__(self):
        self.sample_dates = [
            (20231025, "Is 20231025 a weekday?"),
            (20231026, "Is 20231026 a weekday?"),
            (20231027, "Is 20231027 a weekday?"),
            (20231028, "Is 20231028 a weekday?")
        ]

    def is_weekday(self, date_tuple):
        date_obj = datetime.datetime.fromtimestamp(date_tuple)
        return date_obj.weekday() < 5

if __name__ == '__main__':
    checker = DateChecker()
    for date_tuple, message in checker.sample_dates:
        print(f"{message} {checker.is_weekday(date_tuple)}")