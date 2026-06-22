from datetime import date

class DateChecker:
    def is_weekend(self, date):
        day_of_week = date.weekday()
        return day_of_week >= 5

if __name__ == '__main__':
    checker = DateChecker()
    dates_to_check = {
        '2023-10-06': date(2023, 10, 6),
        '2023-10-07': date(2023, 10, 7),
        '2023-10-08': date(2023, 10, 8)
    }
    for key, value in dates_to_check.items():
        print(f"Is {key} a weekend? {checker.is_weekend(value)}")