def days_in_month(year, month):
    if not isinstance(year, int) or not isinstance(month, int):
        raise ValueError('Year and month must be integers.')
    if year < 1 or month < 1 or month > 12:
        raise ValueError('Invalid year or month.')
    if month == 2:
        is_leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        return 29 if is_leap_year else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
if __name__ == '__main__':
    print(days_in_month(2023, 10))
    print(days_in_month(2024, 2))