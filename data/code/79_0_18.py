import datetime

def calculate_next_month(start_date):
    year = start_date.year
    month = start_date.month
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    return datetime.date(next_year, next_month, start_date.day)

if __name__ == '__main__':
    sample_date_str = "2023-11-30"
    start_date = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    next_date = calculate_next_month(start_date)
    print(next_date.strftime("%Y-%m-%d"))