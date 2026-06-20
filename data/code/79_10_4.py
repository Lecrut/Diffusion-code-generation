import datetime

def get_next_month_date(date):
    if date.month == 12:
        next_year = date.year + 1
        next_month = 1
    else:
        next_year = date.year
        next_month = date.month + 1
    return datetime.date(next_year, next_month, 1)

if __name__ == '__main__':
    sample_date_str = "2023-09-30"
    sample_date = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    next_month_date = get_next_month_date(sample_date)
    print(next_month_date.strftime("%Y-%m-%d"))