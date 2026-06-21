def get_day_of_month(year, month, day):
    if not all(isinstance(v, int) for v in (year, month, day)):
        raise ValueError("Inputs must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be positive")
    leap_check = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_months = (31, 29 if leap_check else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    max_day = days_in_months[month - 1]
    if day > max_day:
        raise ValueError("Day out of range for the given month and year")
    return day

if __name__ == '__main__':
    result = get_day_of_month(2024, 2, 29)
    print(result)