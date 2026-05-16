import datetime
def calculate_time_remaining(target_date_str):
    target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()
    today = datetime.date.today()
    if target_date < today:
        return "Date has passed"
    if target_date.month == 12:
        next_month_start = datetime.date(target_date.year + 1, 1, 1)
    else:
        next_month_start = datetime.date(target_date.year, target_date.month + 1, 1)
    current_month_end = datetime.date(target_date.year, target_date.month + 1, 1) - datetime.timedelta(days=1)
    target_month_end = datetime.date(target_date.year, target_date.month + 1, 1) - datetime.timedelta(days=1)
    days_remaining = (target_month_end - today).days
    return days_remaining
if __name__ == '__main__':
    sample_date = "2024-07-31"
    result = calculate_time_remaining(sample_date)
    print(result)