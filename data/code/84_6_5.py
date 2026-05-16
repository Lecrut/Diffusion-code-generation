import math
def get_day_number(year: int, month: int, day: int) -> int:
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            if day == 29:
                return 60 if month == 2 else 60                                                                                     
            else:
                return day
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29
    day_count = 0
    for m in range(1, month):
        days = days_in_month[m]
        if m == 2 and (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days = 29
        day_count += days
    day_count += day
    return day_count
if __name__ == '__main__':
    print(get_day_number(2023, 1, 1))
    print(get_day_number(2024, 2, 29))
    print(get_day_number(2024, 3, 1))
    print(get_day_number(2023, 12, 31))
    print(get_day_number(2000, 3, 1))
    print(get_day_number(2100, 2, 29))
    print(get_day_number(2100, 2, 28))