from datetime import date

HOLIDAYS = {
    "2023-12-25": True,
    "2024-01-01": True
}

def is_weekend_with_holidays(given_date):
    if not isinstance(given_date, date):
        raise ValueError("Input must be a datetime.date object")
    return given_date.weekday() >= 5 or str(given_date) in HOLIDAYS

if __name__ == '__main__':
    sample_date = date(2023, 12, 26)
    print(is_weekend_with_holidays(sample_date))