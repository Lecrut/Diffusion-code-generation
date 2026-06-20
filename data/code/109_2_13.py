from datetime import date, timedelta

def validate_date(year, month, day):
    if year < 1900 or year > 2100:
        raise ValueError("Year must be between 1900 and 2100")
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12")
    if not 1 <= day <= 31:
        raise ValueError("Day must be between 1 and 31")

def calculate_time_remaining(year, month, day):
    validate_date(year, month, day)
    today = date.today()
    current_month_end = date(year, month, 1) + timedelta(days=32)
    next_month_start = date(current_month_end.year, current_month_end.month % 12 + 1, 1)
    time_remaining = next_month_start - today
    return time_remaining

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    time_left = calculate_time_remaining(sample_year, sample_month, sample_day)
    print(time_left)