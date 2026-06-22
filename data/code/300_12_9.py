def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= year <= 9999 or not 1 <= month <= 12:
        raise ValueError('Year must be between 1 and 9999, and month must be between 1 and 12')
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
if __name__ == '__main__':
    print(days_in_month(2023, 2))
    print(days_in_month(2024, 2))
    print(days_in_month(2023, 4))