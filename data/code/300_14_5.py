def days_in_month(year, month):
    months_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    months_with_30_days = {4, 6, 9, 11}
    if month == 2:
        is_leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        return 29 if is_leap_year else 28
    elif month in months_with_31_days:
        return 31
    elif month in months_with_30_days:
        return 30
if __name__ == '__main__':
    print(days_in_month(2023, 10))
    print(days_in_month(2024, 1))