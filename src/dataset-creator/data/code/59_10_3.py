import datetime
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def get_day_of_week(date_str):
    try:
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
        year, month, day = map(int, parts)
        if not (1 <= month <= 12):
            raise ValueError(f"Invalid month {month}. Must be between 1 and 12.")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap_year(year):
            days_in_month[2] = 29
        max_days = days_in_month[month]
        if not (1 <= day <= max_days):
            raise ValueError(f"Invalid day {day} for month {month}. Must be between 1 and {max_days}.")
    except ValueError as e:
        return str(e)
    try:
        date_obj = datetime.date(year, month, day)
        days_since_epoch = (date_obj - datetime.date(1970, 1, 1)).days % 7
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return f"{day} of {month}/{year} is a {week_days[days_since_epoch]}"
    except Exception as e:
        raise ValueError(f"Date calculation failed due to an unexpected error.")
if __name__ == '__main__':
    sample_dates = [
        "2023-12-25",
        "2024-02-29",
        "2023-02-28",
        "2024-02-28"
    ]
    for date_str in sample_dates:
        result = get_day_of_week(date_str)
        print(result)