def calculate_day(month, year):
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 28
if __name__ == '__main__':
    print(calculate_day(1, 2023))
    print(calculate_day(2, 2024))
    print(calculate_day(2, 2023))
    print(calculate_day(4, 2023))
    print(calculate_day(12, 2023))
    print(calculate_day(2, 2000))