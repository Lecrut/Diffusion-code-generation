import math
def get_day_number(year: int, month: int, day: int) -> int:
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap:
        days_in_month[2] = 29
    day_of_year = 0
    for m in range(1, 13):
        if m == month:
            break
        day_of_year += days_in_month[m]
        if m == 2 and is_leap:
            day_of_year += 1
    if month == 1:
        return day
    cumulative_days = 0
    for m in range(1, month):
        days = 31 if m in (1, 3, 5, 7, 8, 10, 12) else 30
        if m == 2 and is_leap:
            days = 29
        cumulative_days += days
    return cumulative_days + day
if __name__ == '__main__':
    print(get_day_number(2023, 1, 1))
    print(get_day_number(2024, 2, 29))
    print(get_day_number(2024, 3, 1))
    print(get_day_number(2023, 12, 31))
    print(get_day_number(2023, 2, 1))
    print(get_day_number(2023, 2, 28))
    print(get_day_number(2023, 2, 29))
    print(get_day_number(2025, 1, 1))
    print(get_day_number(2000, 3, 1))
    print(get_day_number(2100, 2, 29))