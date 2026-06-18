import datetime
def parse_date(date_string: str) -> datetime.date | None:
    try:
        parts = date_string.split("-")
        if len(parts) != 3:
            return None
        year, month, day = map(int, parts)
        if not (1 <= month <= 12):
            return None
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            days_in_month[2] = 29 if is_leap else 28
        if not (1 <= day <= days_in_month[month]):
            return None
        return datetime.date(year, month, day)
    except ValueError:
        return None
def calculate_days_between(date_str_1: str, date_str_2: str) -> int | None:
    date_obj_1 = parse_date(date_str_1)
    date_obj_2 = parse_date(date_str_2)
    if not (date_obj_1 and date_obj_2):
        return None
    delta = abs((date_obj_2 - date_obj_1).days)
    return delta
if __name__ == '__main__':
    sample_dates = ["2023-05-17", "2024-08-29"]
    result_days = calculate_days_between(sample_dates[0], sample_dates[1])
    if result_days is not None:
        print(f"Days between {sample_dates[0]} and {sample_dates[1]}: {result_days}")
    else:
        print("Invalid date format provided.")