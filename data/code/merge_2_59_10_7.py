import datetime
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def get_day_of_week(date_str: str) -> int:
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD.") from e
    if not (1 <= date_obj.day <= 30):
        max_days_in_month = [31] * 7 + [28, 31, 30, 31, 30, 31, 31]
        month_idx = date_obj.month - 1
        if is_leap_year(date_obj.year):
            max_days_in_month[1] = 29
        if not (date_obj.day <= max_days_in_month[month_idx]):
            raise ValueError(f"Invalid day for the given month in {date_str}.")
    return date_obj.weekday()
if __name__ == '__main__':
    sample_dates = [
        "2023-12-25",
        "2024-02-29",
        "2023-02-28"
    ]
    for date_str in sample_dates:
        try:
            day_index = get_day_of_week(date_str)
            print(f"{date_str} is a {day_index}")
        except ValueError as ve:
            print(f"Error processing {date_str}: {ve}")