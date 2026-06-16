def calculate_ordinal_day(month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0:
        days_in_month[2] = 29
    elif year % 100 == 0:
        days_in_month[2] = 28
    if year % 400 == 0:
        days_in_month[2] = 29
    if 1 <= month <= 12:
        return days_in_month[month]
    else:
        raise ValueError("Invalid month number")
if __name__ == '__main__':
    print(calculate_ordinal_day(1, 2023))
    print(calculate_ordinal_day(2, 2024))
    print(calculate_ordinal_day(2, 2000))
    print(calculate_ordinal_day(4, 2023))
    print(calculate_ordinal_day(12, 2023))