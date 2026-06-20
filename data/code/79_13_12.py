import datetime

def get_next_month_date(start_date):
    year = start_date.year + start_date.month // 12
    month = start_date.month % 12 + 1
    return datetime.date(year, month, 1)
if __name__ == '__main__':
    sample_date = datetime.date(2023, 1, 15)
    next_month_start = get_next_month_date(sample_date)
    print(next_month_start.strftime('%Y-%m-%d'))