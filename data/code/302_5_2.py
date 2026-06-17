def calculate_day(month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            days_in_month[2] = 29
    day_number = days_in_month[month]
    return day_number
if __name__ == '__main__':
    print(calculate_day(1, 2023))
    print(calculate_day(2, 2024))
    print(calculate_day(2, 2023))
    print(calculate_day(4, 2023))
    print(calculate_day(2, 2100))
    print(calculate_day(2, 2000))