import calendar
def get_weekday(year: int, month: int, day: int) -> int:
    if not isinstance(year, (int, float)) or not isinstance(month, (int, float)) or not isinstance(day, (int, float)):
        raise TypeError("All arguments must be integers.")
    year = int(year)
    month = int(month)
    day = int(day)
    if month < 1 or month > 12:
        raise ValueError(f"Month {month} is out of range (1-12).")
    try:
        calendar_day = calendar.monthrange(year, month)[1] + day - 1
        weekday_num = ((calendar_day % 7) + 6) % 7 + 1
        return int(weekday_num)
    except ValueError as e:
        raise ValueError(f"Invalid date combination for {year}, {month}, {day}: {e}")
if __name__ == '__main__':
    sample_data = [
        (2023, 5, 1),
        (2024, 6, 15),
        (2023, 7, 4)
    ]
    for item in sample_data:
        if isinstance(item[0], int):
            result = get_weekday(*item)
        else:
            year, month, day = item
            try:
                weekday_num = ((calendar_day % 7) + 6) % 7 + 1
                print(f"{year}, {month}, {day} -> Weekday Number: {weekday_num}")
            except ValueError as e:
                print(f"Error for {item}: {e}")