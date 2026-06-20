import datetime

class DateEvaluator:
    def __init__(self):
        self.weekdays = set(range(5))

    def is_weekday(self, date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return date_obj.weekday() in self.weekdays
        except ValueError:
            return False

if __name__ == '__main__':
    evaluator = DateEvaluator()
    test_dates = [
        "2023-10-23",
        "2023-10-24",
        "2023-10-25",
        "2023-10-26",
        "2023-10-27",
        "2023-10-28",
        "2023-10-29"
    ]
    for date_str in test_dates:
        result = evaluator.is_weekday(date_str)
        print(f"Date: {date_str}, Is Weekday: {result}")