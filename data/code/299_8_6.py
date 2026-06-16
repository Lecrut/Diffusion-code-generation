class WeekendChecker:
    def __init__(self):
        pass
    def check_date(self, date):
        import datetime
        weekday = datetime.date.fromisoformat(date).weekday()
        return weekday >= 5
    def filter_dates(self, date_list):
        result = []
        for date in date_list:
            if self.check_date(date):
                result.append(date)
        return result
if __name__ == '__main__':
    checker = WeekendChecker()
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2023-10-29",
        "2023-10-30",
        "2023-10-31"
    ]
    print("Checking individual dates:")
    for date_str in sample_dates:
        is_weekend = checker.check_date(date_str)
        print(f"{date_str}: Weekend? {is_weekend}")
    print("\nFiltering list of dates:")
    weekend_dates = checker.filter_dates(sample_dates)
    print(f"Weekend dates found: {weekend_dates}")