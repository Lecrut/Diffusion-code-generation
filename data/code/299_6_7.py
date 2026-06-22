from datetime import date
HOLIDAYS = [date(2023, 12, 25), date(2024, 1, 1)]

def is_weekend_with_holidays(given_date):
    return given_date.weekday() >= 5 or given_date in HOLIDAYS
if __name__ == '__main__':
    print(is_weekend_with_holidays(date(2023, 12, 25)))
    print(is_weekend_with_holidays(date(2024, 1, 1)))
    print(is_weekend_with_holidays(date(2024, 1, 2)))