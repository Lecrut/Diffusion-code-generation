import datetime

class DateChecker:
    def __init__(self):
        self.weekday_names = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday'
        }

    def is_weekday(self, date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            weekday = date_obj.weekday()
            return 0 <= weekday <= 4
        except ValueError:
            return False

    def get_weekday_name(self, date_str):
        if self.is_weekday(date_str):
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            weekday = date_obj.weekday()
            return self.weekday_names[weekday]
        else:
            return "Invalid date"

if __name__ == '__main__':
    checker = DateChecker()
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
        is_weekday = checker.is_weekday(date_str)
        weekday_name = checker.get_weekday_name(date_str)
        print(f"Date: {date_str}, Is Weekday: {is_weekday}, Day Name: {weekday_name}")