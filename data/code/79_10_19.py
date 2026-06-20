import datetime

def get_next_month_date(date):
    year = date.year + (date.month == 12)
    month = (date.month % 12) + 1
    return datetime.date(year, month, 1)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 4, 15)
    next_month_date = get_next_month_date(sample_date)
    print(next_month_date)