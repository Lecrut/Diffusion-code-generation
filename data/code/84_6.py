def get_day_number(year: int, month: int, day: int) -> int:
    if year < 1:
        raise ValueError("Year must be positive")
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap:
        days_in_month[2] = 29
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    day_of_year = 0
    for m in range(1, month):
        day_of_year += days_in_month[m]
    day_of_year += day
    return day_of_year
if __name__ == '__main__':
    print(get_day_number(2023, 1, 1))
    print(get_day_number(2024, 2, 29))
    print(get_day_number(2024, 3, 1))
    print(get_day_number(2023, 12, 31))
    print(get_day_number(2024, 2, 1))
    print(get_day_number(2023, 2, 28))
    print(get_day_number(2023, 2, 29))
    print(get_day_number(2000, 3, 1))
    print(get_day_number(2100, 2, 29))