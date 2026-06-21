import calendar

def get_day_of_month(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    _, max_days = calendar.monthrange(year, month)
    if not (1 <= day <= max_days):
        raise ValueError("Day is out of range for the given month and year")
    return day

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    result = get_day_of_month(year, month, day)
    print(result)