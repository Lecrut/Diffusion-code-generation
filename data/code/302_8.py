def get_ordinal_day(month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days_in_month[2] = 29 if is_leap else 28
    return days_in_month[month]
if __name__ == '__main__':
    print(get_ordinal_day(1, 2023))
    print(get_ordinal_day(2, 2024))
    print(get_ordinal_day(4, 2023))
    print(get_ordinal_day(12, 2022))
    print(get_ordinal_day(2, 2000))