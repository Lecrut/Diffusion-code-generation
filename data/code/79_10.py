import datetime
def calculate_next_month(start_date):
    if start_date.month == 12:
        next_month = 1
        next_year = start_date.year + 1
    else:
        next_month = start_date.month + 1
        next_year = start_date.year
    return datetime.date(next_year, next_month, 1)
if __name__ == '__main__':
    start_date_str = "2023-12-15"
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    next_date = calculate_next_month(start_date)
    print(next_date.strftime("%Y-%m-%d"))