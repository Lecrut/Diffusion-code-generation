from datetime import datetime, timedelta

def calculate_next_month(start_date):
    if start_date is None:
        return None
    try:
        next_month = start_date.replace(month=start_date.month + 1)
    except ValueError:
        next_month = start_date.replace(year=start_date.year + 1, month=1)
    if next_month.day != start_date.day:
        last_day_of_next_month = next_month.replace(day=28) + timedelta(days=4)
        next_month = next_month.replace(day=min(start_date.day, last_day_of_next_month.day))
    return next_month
if __name__ == '__main__':
    start_date_str = '2023-12-31'
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    next_date = calculate_next_month(start_date)
    print(next_date.strftime('%Y-%m-%d'))