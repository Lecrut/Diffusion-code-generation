def days_in_month(year, month):
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return 29 if is_leap else 28
    elif month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    else:
        return 30
if __name__ == '__main__':
    year = 2024
    month = 2
    result = days_in_month(year, month)
    print(result)