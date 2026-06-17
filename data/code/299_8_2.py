class WeekendChecker:
    def __init__(self):
        pass
    def check_date(self, date):
        import datetime
        weekday = datetime.date.fromisoformat(date).weekday()
        return weekday >= 5
    def filter_dates(self, date_list):
        return [date for date in date_list if self.check_date(date)]
if __name__ == '__main__':
    checker = WeekendChecker()
    sample_dates = [
        "2023-10-21",
        "2023-10-22",
        "2023-10-23",
        "2023-10-24",
        "2023-10-25",
        "2023-10-26",
        "2023-10-27"
    ]
    print("Checking individual dates:")
    for date in sample_dates:
        is_weekend = checker.check_date(date)
        print(f"{date}: Weekend? {is_weekend}")
    print("\nFiltering list of dates:")
    weekend_dates = checker.filter_dates(sample_dates)
    print("Weekend dates found:")
    print(weekend_dates)