from datetime import date

def calculate_days_remaining() -> int:
    today = date.today()
    last_day_of_month = date(today.year, today.month, 1) + dateutil.relativedelta.relativedelta(months=+1) - dateutil.relativedelta.relativedelta(days=+1)
    days_remaining = (last_day_of_month - today).days
    return days_remaining

if __name__ == '__main__':
    remaining_days = calculate_days_remaining()
    print(f"Days remaining in this month: {remaining_days}")