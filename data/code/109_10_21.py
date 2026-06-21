import datetime

def get_days_remaining_in_month(year, month):
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if year < 1:
        raise ValueError("Invalid year")
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    last_day = next_month_start - datetime.timedelta(days=1)
    today = datetime.date.today()
    if today.year != year or today.month != month:
        return 0
    return (last_day - today).days

if __name__ == '__main__':
    print(get_days_remaining_in_month(2023, 10))
    print(get_days_remaining_in_month(2024, 2))
    print(get_days_remaining_in_month(2023, 12))