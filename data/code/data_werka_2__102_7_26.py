import calendar
from datetime import date

WEEKDAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

class DateChecker:
    def __init__(self, target_date):
        self.target_date = target_date

    def is_weekday(self):
        try:
            day_index = calendar.weekday(
                self.target_date.year,
                self.target_date.month,
                self.target_date.day
            )
            return day_index < 5
        except AttributeError:
            return False

    def get_name(self):
        try:
            day_index = calendar.weekday(
                self.target_date.year,
                self.target_date.month,
                self.target_date.day
            )
            return WEEKDAY_NAMES.get(day_index, "Unknown")
        except AttributeError:
            return "Unknown"

if __name__ == '__main__':
    test_date = date(2024, 5, 15)
    checker = DateChecker(test_date)
    weekday_status = checker.is_weekday()
    day_name = checker.get_name()
    print(f"{weekday_status} for {day_name}")