from datetime import date, timedelta

def calculate_days_remaining() -> int:
    today = date.today()
    year, month, _ = today.year, today.month, today.day
    last_day_of_month = date(year, month + 1, 1) - timedelta(days=1)
    days_remaining = (last_day_of_month - today).days
    return days_remaining

if __name__ == '__main__':
    remaining_days = calculate_days_remaining()
    print(f"Days remaining in this month: {remaining_days}")