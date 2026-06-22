from datetime import date

def is_weekend_with_holidays(date_obj):
    weekend_days = {5, 6}
    holidays = {date(2023, 12, 25), date(2024, 1, 1)}
    return date_obj.weekday() in weekend_days or date_obj in holidays
if __name__ == '__main__':
    sample_date = date(2023, 12, 25)
    print(is_weekend_with_holidays(sample_date))