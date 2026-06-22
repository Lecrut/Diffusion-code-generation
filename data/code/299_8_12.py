from datetime import date

class DateChecker:
    def __init__(self):
        self.holidays = {'2023-10-13', '2023-10-14', '2023-10-15'}

    def is_weekend_or_holiday(self, date_str):
        return date.fromisoformat(date_str).weekday() >= 5 or date_str in self.holidays

if __name__ == '__main__':
    checker = DateChecker()
    dates_to_check = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = {date: checker.is_weekend_or_holiday(date) for date in dates_to_check}
    print(results)