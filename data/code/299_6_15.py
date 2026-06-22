from datetime import date

def is_weekend_with_holidays(date_to_check):
    holidays = [date(2023, 12, 25), date(2024, 1, 1)]
    return date_to_check.weekday() >= 5 or date_to_check in holidays
if __name__ == '__main__':
    print(is_weekend_with_holidays(date(2023, 12, 26)))
    print(is_weekend_with_holidays(date(2024, 1, 2)))