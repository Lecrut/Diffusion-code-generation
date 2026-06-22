import datetime
holidays = [datetime.date(2023, 12, 25), datetime.date(2024, 1, 1)]

def is_weekend_with_holidays(date):
    return date.weekday() >= 5 or date in holidays
if __name__ == '__main__':
    sample_date = datetime.date(2023, 12, 26)
    print(is_weekend_with_holidays(sample_date))