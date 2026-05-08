import calendar
def is_valid_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return False
    if month < 1 or month > 12:
        return False
    if not (1 <= day <= 31):
        return False
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = calendar.isleap(year)
    if is_leap:
        days_in_month[2] = 29
    if day > days_in_month[month]:
        return False
    return True
if __name__ == '__main__':
    test_dates = [
        (2023, 10, 26),
        (2024, 2, 29),
        (2023, 2, 29),
        (2023, 13, 1),
        (2023, 40, 1),
        (2024, 2, 30),
        (2023, 12, 32),
        (2024, 13, 1)
    ]
    for year, month, day in test_dates:
        result = is_valid_date(year, month, day)
        print(f"Date ({year}, {month}, {day}) is valid: {result}")