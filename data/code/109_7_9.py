from datetime import date, timedelta

def get_days_in_month(year: int, month: int) -> int:
    if month == 12:
        return (date(year + 1, 1, 1) - date(year, month, 1)).days
    else:
        return (date(year, month + 1, 1) - date(year, month, 1)).days

def calculate_seconds_remaining_in_month() -> int:
    today = date.today()
    days_in_current_month = get_days_in_month(today.year, today.month)
    seconds_per_day = 24 * 60 * 60
    return (date(today.year, today.month, 1) + timedelta(days=days_in_current_month - 1)) - today

if __name__ == '__main__':
    result = calculate_seconds_remaining_in_month()
    print(result)