import datetime

def get_next_month_date(date):
    year = date.year
    month = date.month + 1 if date.month < 12 else 1
    if month == 1:
        year += 1
    return datetime.date(year, month, 1)

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 9, 30)
    next_month_date = get_next_month_date(sample_date)
    print(next_month_date.strftime("%Y-%m-%d"))