from datetime import date

HOLIDAYS = [date(2023, 12, 25), date(2024, 1, 1)]

def is_weekend_with_holidays(date_to_check):
    return date_to_check.weekday() >= 5 or date_to_check in HOLIDAYS

if __name__ == '__main__':
    sample_date = date(2023, 12, 26)
    print(is_weekend_with_holidays(sample_date))