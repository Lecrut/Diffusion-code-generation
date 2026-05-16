import datetime
def calculate_next_month(start_date):
    if start_date is None:
        return None
    year = start_date.year
    month = start_date.month
    day = start_date.day
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    return datetime.date(next_year, next_month, day)
if __name__ == '__main__':
    start_date_str = "2023-12-31"
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    next_date = calculate_next_month(start_date)
    print(next_date.strftime("%Y-%m-%d"))