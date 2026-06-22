def get_day_of_month(year, month, day):
    if not isinstance(year, int) or isinstance(year, bool):
        raise ValueError("Year must be an integer")
    if not isinstance(month, int) or isinstance(month, bool):
        raise ValueError("Month must be an integer")
    if not isinstance(day, int) or isinstance(day, bool):
        raise ValueError("Day must be an integer")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be positive")
    leap_condition = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_current_month = 31
    if month in (4, 6, 9, 11):
        days_in_current_month = 30
    elif month == 2:
        days_in_current_month = 29 if leap_condition else 28
    if day > days_in_current_month:
        raise ValueError("Day out of range for the given month and year")
    return day

if __name__ == '__main__':
    result = get_day_of_month(2024, 2, 29)
    print(result)