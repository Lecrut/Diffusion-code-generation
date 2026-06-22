from datetime import date

class WeekendChecker:
    def is_weekend(self, date_str):
        dt = date.fromisoformat(date_str)
        return dt.weekday() >= 5

if __name__ == '__main__':
    checker = WeekendChecker()
    dates = ['2023-10-06', '2023-10-07', '2023-10-08']
    results = {date_str: checker.is_weekend(date_str) for date_str in dates}
    for date_str, is_weekend in results.items():
        print(f"Is {date_str} a weekend? {is_weekend}")