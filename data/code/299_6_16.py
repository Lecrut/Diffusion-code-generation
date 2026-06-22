from datetime import date

WEEKEND_DAYS = {5, 6}
HOLIDAYS = {
    "2023-12-25": True,
    "2024-01-01": True
}

def is_weekend_with_holidays(given_date):
    return given_date.weekday() in WEEKEND_DAYS or str(given_date) in HOLIDAYS

if __name__ == '__main__':
    sample_date = date(2023, 12, 26)
    print(is_weekend_with_holidays(sample_date))