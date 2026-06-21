def extract_day_from_date(year, month, day):
    days_per_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Inputs must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be positive")
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    max_days = days_per_month[month]
    if month == 2 and is_leap_year:
        max_days += 1
    if day > max_days:
        raise ValueError("Day out of range for the given month and year")
    return day

if __name__ == '__main__':
    current_year = 2024
    current_month = 2
    current_day = 29
    day_value = extract_day_from_date(current_year, current_month, current_day)
    print(day_value)