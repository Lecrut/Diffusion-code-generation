from datetime import date

def calculate_days_remaining() -> int:
    today = date.today()
    last_day_of_month = date(today.year, today.month, 1) + timedelta(days=31)
    if last_day_of_month.month != today.month:
        last_day_of_month -= timedelta(days=last_day_of_month.day)
    return (last_day_of_month - today).days

if __name__ == '__main__':
    remaining_days = calculate_days_remaining()
    print(f"Days remaining in this month: {remaining_days}")