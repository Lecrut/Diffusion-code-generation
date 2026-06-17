import datetime
def parse_date(date_string: str) -> datetime.date | None:
    try:
        parts = date_string.split('-')
        if len(parts) != 3:
            return None
        year, month, day_str = map(int, parts)
        if not (1 <= year <= 9999):
            return None
        if not (1 <= month <= 12):
            return None
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[2] = 29
        max_days = days_in_month[month]
        if not (1 <= day_str <= max_days):
            return None
        date_obj = datetime.date(year, month, int(day_str))
        return date_obj
    except ValueError:
        return None
def calculate_day_difference(date_string_1: str, date_string_2: str) -> int | None:
    if not isinstance(date_string_1, str) or not isinstance(date_string_2, str):
        return None
    parsed_date_1 = parse_date(date_string_1)
    parsed_date_2 = parse_date(date_string_2)
    if parsed_date_1 is None or parsed_date_2 is None:
        return None
    delta_days = (parsed_date_2 - parsed_date_1).days
    return abs(delta_days)
if __name__ == '__main__':
    sample_dates = ["2023-05-15", "2024-08-20"]
    result = calculate_day_difference(sample_dates[0], sample_dates[1])
    if result is not None:
        print(f"Days between {sample_dates[0]} and {sample_dates[1]}: {result}")
    else:
        print("Error: Invalid date format provided.")