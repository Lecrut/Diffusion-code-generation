import datetime

def compute_weekday(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Arguments must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    try:
        date_instance = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
    return date_instance.strftime("%A")

if __name__ == '__main__':
    target_year = 2024
    target_month = 2
    target_day = 29
    weekday_name = compute_weekday(target_year, target_month, target_day)
    print(weekday_name)