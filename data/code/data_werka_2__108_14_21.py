def get_day_of_month(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Inputs must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be positive")
    days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    max_day = days_in_months[month - 1]
    if month == 2 and is_leap:
        max_day += 1
    if day > max_day:
        raise ValueError("Day out of range for the given month and year")
    return day

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    result = get_day_of_month(sample_year, sample_month, sample_day)
    print(result)