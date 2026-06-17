class WeekendChecker:
    def __init__(self):
        pass
    def check_date(self, date):
        import datetime
        try:
            d = datetime.datetime.strptime(str(date), "%Y-%m-%d").date()
            return d.weekday() >= 5
        except ValueError:
            return False
    def filter_dates(self, date_list):
        filtered_list = []
        for date in date_list:
            if self.check_date(date):
                filtered_list.append(date)
        return filtered_list
if __name__ == '__main__':
    checker = WeekendChecker()
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2023-10-29",
        "2023-10-30",
        "2023-10-31",
        "2023-11-01"
    ]
    print("Checking individual dates:")
    for date_str in sample_dates:
        is_weekend = checker.check_date(date_str)
        print(f"{date_str}: Weekend? {is_weekend}")
    print("\nFiltering list of dates:")
    weekend_dates = checker.filter_dates(sample_dates)
    print("Weekend dates found:", weekend_dates)