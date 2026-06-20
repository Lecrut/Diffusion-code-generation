import datetime

class DateChecker:
    def __init__(self, date_strings):
        self.date_strings = date_strings

    def is_weekday(self, date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            weekday = date_obj.weekday()
            return 0 <= weekday <= 4
        except ValueError:
            return False

    def check_all_dates(self):
        results = {date_str: self.is_weekday(date_str) for date_str in self.date_strings}
        return results

if __name__ == '__main__':
    checker = DateChecker(["2023-10-27", "2024-02-29", "2023-10-28", "2023-02-28"])
    print(checker.check_all_dates())