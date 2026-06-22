def days_in_month(year, month):
    if month == 2:
        is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        return 29 if is_leap else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

if __name__ == '__main__':
    print(days_in_month(2023, 2))
    print(days_in_month(2024, 2))
    print(days_in_month(2023, 4))