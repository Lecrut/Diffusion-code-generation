from datetime import datetime

class DateChecker:

    def __init__(self):
        self.holidays = {'2023-10-12'}

    def is_weekend(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            weekday = date_obj.weekday()
            return weekday >= 5
        except ValueError:
            return False

    def is_holiday(self, date_str):
        return date_str in self.holidays
if __name__ == '__main__':
    checker = DateChecker()
    sample_date = '2023-10-12'
    print(checker.is_weekend(sample_date))
    print(checker.is_holiday(sample_date))