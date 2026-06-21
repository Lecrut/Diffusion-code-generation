import calendar

def validate_date_components(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Year, month, and day must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be positive")
    max_days = calendar.monthrange(year, month)[1]
    if day > max_days:
        raise ValueError(f"Day {day} is out of range for {year}-{month}")
    return True

def is_weekday(year, month, day):
    validate_date_components(year, month, day)
    return calendar.weekday(year, month, day) < 5

if __name__ == '__main__':
    result = is_weekday(2023, 10, 23)
    print(result)
    result2 = is_weekday(2023, 10, 28)
    print(result2)
    result3 = is_weekday(2024, 2, 29)
    print(result3)