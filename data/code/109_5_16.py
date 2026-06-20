import datetime

def get_last_day_of_month(year: int, month: int) -> datetime.date:
    if month == 12:
        return datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        next_month = month + 1
        next_year = year if next_month < 13 else year + 1
        return datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)

def calculate_remaining_minutes(year: int, month: int) -> int:
    today = datetime.date.today()
    last_day_of_current_month = get_last_day_of_month(today.year, today.month)
    days_left = (last_day_of_current_month - today).days
    minutes_left = days_left * 24 * 60
    return minutes_left

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    print(calculate_remaining_minutes(sample_year, sample_month))