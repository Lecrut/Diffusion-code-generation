import calendar
def get_weekday(year: int, month: int, day: int) -> int:
    if not isinstance(year, (int, float)) or year < 1678 or year > 9999:
        raise ValueError("Invalid year")
    try:
        month = int(month)
        day = int(day)
    except TypeError:
        raise ValueError("Month and day must be integers")
    if not isinstance(month, (int, float)) or month < 1 or month > 12:
        raise ValueError("Invalid month")
    if not isinstance(day, (int, float)):
        raise ValueError("Day must be an integer")
    try:
        day = int(day)
    except ValueError:
        pass
    if day < 1 or day > calendar.monthrange(year, month)[1]:
        raise ValueError(f"Invalid day for {year}-{month}")
    return calendar.weekday(year, month, day) + 1
if __name__ == '__main__':
    sample_tuple = (2023, 5, 1)
    result_tuple = get_weekday(*sample_tuple)
    print(f"Input tuple: {sample_tuple}")
    print(f"Weekday number ({result_tuple}): Monday=1 to Sunday=7")
    test_cases = [
        (2023, 5, 1),
        (2024, 1, 1),
        (2023, 6, 15)
    ]
    for tc in test_cases:
        print(f"Input tuple: {tc}")
        weekday = get_weekday(*tc)
        days_map = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_name = days_map[weekday - 1]
        print(f"Weekday number ({weekday}): {day_name}")