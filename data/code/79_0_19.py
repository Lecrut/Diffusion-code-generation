import datetime

def calculate_next_month(start_date):
    if start_date is None:
        return None
    try:
        next_month = start_date.replace(day=1) + datetime.timedelta(days=32)
        return next_month.replace(day=1)
    except ValueError:
        return start_date.replace(month=start_date.month + 1, day=1)

if __name__ == '__main__':
    start_date_str = "2023-12-31"
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    next_date = calculate_next_month(start_date)
    print(next_date.strftime("%Y-%m-%d"))